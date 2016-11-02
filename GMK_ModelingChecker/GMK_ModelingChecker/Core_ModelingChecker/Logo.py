# -*- coding:utf-8 -*-

from PySide import QtGui, QtCore

from Core_ModelingChecker import utils
reload(utils)

class Logo(QtGui.QLabel):
    def __init__(self, parent=None):
        super(Logo, self).__init__(parent)

        logoImage = QtGui.QPixmap(utils.getIconPath() +'logo.png')
        self.setAlignment(QtCore.Qt.AlignRight)
        self.setPixmap(logoImage.scaled(150,50, QtCore.Qt.KeepAspectRatio))
        # Set Widget
        self.setWindowTitle("Logo")
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = Logo()
    ui.show()
    sys.exit(app.exec_())