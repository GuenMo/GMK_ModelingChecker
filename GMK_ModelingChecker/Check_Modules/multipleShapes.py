# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

CLASS_NAME = "MultipleShapes"

TITLE = "Multiple Shapes"
DESCRIPTION = u"한 트렌스폼 노드에 여러게의 쉐입이 존재 하는지 검사를 합니다."
BUTTONS = ["Check", "Select", "Delete"]

class MultipleShapes(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(MultipleShapes, self).__init__()
    
        
    def Check(self):
        allShape = self.findAllShapes()
        intermediateObjects = []
        
        for shape in allShape:
            if shape.intermediateObject.get():
                intermediateObjects.append(shape)
            
        return intermediateObjects
    
#     def Select(self, nodes):
#         return self.Select_tramsformFromShape(nodes)
    
    
        