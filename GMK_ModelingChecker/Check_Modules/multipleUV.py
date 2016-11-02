# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)


CLASS_NAME = "MultipleUV"

TITLE = "Multiple UV Set"
DESCRIPTION = u"한 메쉬에 2개 이상의 UV가 있는지 검사 합니다."
BUTTONS = ["Check", "Select", "Print"]

class MultipleUV(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(MultipleUV, self).__init__()
    
        
    def Check(self):
        allShape = self.findAllShapes()
        nodes = []
        
        for shape in allShape:
            if len(shape.getUVSetNames()) > 1:
                nodes.append(shape)
        return nodes
    
    def Execute(self, nodes):
        for node in nodes:
            print "UVs : " , node.getUVSetNames() 
    
    
        