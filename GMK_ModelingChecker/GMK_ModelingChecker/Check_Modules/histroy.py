# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

import pymel.core as pm


CLASS_NAME = "History"

TITLE = "History"
DESCRIPTION = u"메쉬에 히스토리 있는지를 검사 합니다."
BUTTONS = ["Check", "Select", "Delete"]

class History(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(History, self).__init__()
    
    def Check(self):
        allShapes = self.findAllShapes()
        
        nodes = []
        for shape in allShapes:
            if len(shape.inputs()) != 0:
                nodes.append(shape)
        
        return nodes
    
#     def Select(self, nodes):
#         return self.Select_tramsformFromShape(nodes)
    
    def Execute(self, nodes):
        for node in nodes:
            pm.delete(node, ch=True)

    
    
            