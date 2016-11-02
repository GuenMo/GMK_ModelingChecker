# -*- coding:utf-8 -*-

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    
import stylesheet
import utils as utils
reload(utils)

import Logo as Logo
reload(Logo)

from functools import partial

__version__ = "1.2.0"

class ModelingChekerWindow(QMainWindow):
    def __init__(self, parent=utils.getMayaWindow()):
        super(ModelingChekerWindow, self).__init__(parent)
         
        self.iconPath = utils.getIconPath()
        self.CheckedReuslt = None
        self.initUI()
        
    def initUI(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.main_Layout = QVBoxLayout()
        self.centralWidget.setLayout(self.main_Layout)
        
        #self.Logo = Logo.Logo()
        #self.main_Layout.addWidget(self.Logo)
        
        self.scroll = self.initialiseModuelList()
        self.main_Layout.addWidget(self.scroll)
        
        self.main_Layout.addStretch()
        self.main_Layout.addLayout(self.createButtons())
        
        self.setFixedWidth(340)
        self.setWindowTitle("Modeling Checker")
        
    def initialiseModuelList(self):
        moduleListWidget = QWidget()
        moduleListLayout = QVBoxLayout()
        moduleListWidget.setLayout(moduleListLayout)
          
        for module in utils.findAllModuel("/Check_Modules"):
            moduleWidget = self.createModuleWidge(module)
            moduleListLayout.addLayout(moduleWidget)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(540)
        scroll.setWidget(moduleListWidget)
        
        return scroll
        
    def createModuleWidge(self, module):
        mod = __import__("Check_Modules." + module, {}, {}, [module])
        reload(mod)
        
        layoutName = module + "Layout"
        title = mod.TITLE
        description = mod.DESCRIPTION
        buttons = mod.BUTTONS
        
        moduleLayout = QGridLayout()
        moduleLayout.setObjectName(layoutName)
        moduleLabel = QLabel(title)
        moduleLabel.setFixedSize(100, 20)
        moduleLabel.setToolTip(description)
        moduleLayout.addWidget(moduleLabel, 0,0)
        
        i = 1
        for btn in buttons:
            moduleButton = QPushButton(btn)
            moduleButton.setFixedHeight(20)                
            moduleButton.setToolTip(description)
            moduleLayout.addWidget(moduleButton, 0,i)
            
            if btn == "Check":
                moduleButton.clicked.connect(partial(self.Check, module))  
            elif btn == "Select":
                moduleButton.clicked.connect(partial(self.Select, module))
                moduleButton.setEnabled(False)
            else :
                moduleButton.clicked.connect(partial(self.Execute, module))
                moduleButton.setEnabled(False)
            i += 1
        
        statusLabel = QLabel()
        statusLabel.setFixedSize(20,20)
        statusIcon = QPixmap(self.iconPath + "/default.png")
        
        width = statusLabel.width()
        height = statusLabel.height()
        statusLabel.setPixmap(statusIcon.scaled(width,height))
        statusLabel.setObjectName(module + "statusLabel")
        moduleLayout.addWidget(statusLabel, 0, i+1)
        
        return moduleLayout
            
    def Check(self, module):
        moduleInstance = self.instantizeModule(module)
        
        moduleWidgets   = self.getModuleWidgets(module)
        statusLabel     = moduleWidgets[0]
        buttons         = moduleWidgets[1]
        
        # module instance function 
        self.CheckedReuslt = moduleInstance.Check()
        if len(self.CheckedReuslt) == 0:
            self.CheckedReuslt = None
            
        self.changeStatus(statusLabel, buttons)
          
    def Select(self, module):
        self.Check(module)
        moduleInstance = self.instantizeModule(module)
        
        self.CheckedReuslt = moduleInstance.Check()
        if len(self.CheckedReuslt) == 0:
            self.CheckedReuslt = None
            
        if self.CheckedReuslt != None:
            sels = moduleInstance.Select(self.CheckedReuslt)
            return sels
        else:
            return None
  
    def Execute(self, module):
        moduleInstance = self.instantizeModule(module)
        
        self.CheckedReuslt = moduleInstance.Check()
        if len(self.CheckedReuslt) == 0:
            self.CheckedReuslt = None
        
        if self.CheckedReuslt != None:
            moduleInstance.Execute(self.CheckedReuslt)
        self.Check(module)
        
    def instantizeModule(self, module):
        mod = __import__("Check_Modules."+module, {}, {}, [module])
        reload(mod)
        moduleClass = getattr(mod, mod.CLASS_NAME)
        moduleInstance = moduleClass()
        
        return moduleInstance
    
    def getModuleWidgets(self, module, widgetType = QGridLayout):
        moduleWidget = self.scroll.findChild(QGridLayout, module + "Layout")
        statusLabel = None
        buttons = []
        
        for i in range(moduleWidget.count()):
            widget = moduleWidget.itemAt(i).widget()
            if i > 1 and widget.objectName() == module + "statusLabel":
                statusLabel = widget
            elif type(widget) == QPushButton:
                buttons.append(widget)
        
        return (statusLabel, buttons)
    
    def changeStatus(self, statusLabel, buttons):
        statusIcon = None
        
        if self.CheckedReuslt != None:
            for i in range(1,len(buttons)):
                buttons[i].setEnabled(True)
            statusIcon = QPixmap(self.iconPath + "/error.png")
        else:
            for i in range(1,len(buttons)):
                buttons[i].setEnabled(False)
            statusIcon = QPixmap(self.iconPath + "/fixed.png")
        
        if statusLabel != None:
            width = statusLabel.width()
            height = statusLabel.height()
            statusLabel.setPixmap(statusIcon.scaled(width,height))
    
    def createButtons(self):
        buttonslayout = QHBoxLayout()
        checkAll_Button = QPushButton("Check All")
        excuteAll_Button = QPushButton("Execute All")
        reset_Button = QPushButton("Reset")
        buttonslayout.addWidget(checkAll_Button)
        buttonslayout.addWidget(excuteAll_Button)
        buttonslayout.addWidget(reset_Button)
        
        checkAll_Button.clicked.connect(self.checkAll)
        excuteAll_Button.clicked.connect(self.executeAll)
        reset_Button.clicked.connect(self.reset)
        return buttonslayout
    
    def checkAll(self):
        modules = utils.findAllModuel("/Check_Modules")
        step = len(modules)
        pd = QProgressDialog("Checking in progress.",None, 0, step)
        pd.show()
        
        i = 0
        for module in modules:
            pd.setLabelText(module + " checking in progress.")
            pd.setValue(i)
            self.Check(module)
            i += 1
        
    def executeAll(self):
        modules = utils.findAllModuel("/Check_Modules")
        step = len(modules)
        pd = QProgressDialog("Checking in progress.",None, 0, step)
        pd.show()
        
        i = 0
        for module in modules:
            pd.setLabelText(module + " executing in progress.")
            pd.setValue(i)
            self.Execute(module)
            i += 1

    def reset(self):
        for module in utils.findAllModuel("/Check_Modules"):
            widgets = self.getModuleWidgets(module)
            self.resetStatus(widgets[0], widgets[1])
             
    def resetStatus(self, statusLabel, buttons):
        for i in range(1,len(buttons)):
            buttons[i].setEnabled(False)
        statusIcon = QPixmap(self.iconPath + "/default.png")
        width = statusLabel.width()
        height = statusLabel.height()
        statusLabel.setPixmap(statusIcon.scaled(width,height))

         
def main():
    global win
    try:
        win.close()
        win.deleteLater()
    except:
        pass
    win = ModelingChekerWindow()
    win.show()

        
        
        
        
        