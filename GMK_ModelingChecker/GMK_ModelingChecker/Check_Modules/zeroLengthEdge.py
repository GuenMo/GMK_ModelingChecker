# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)
import pymel.core as pm


CLASS_NAME = "ZeroLengthEdge"

TITLE = "Zero Length Edge"
DESCRIPTION = u"길이가 0인 엣지를 검사 합니다."
BUTTONS = ["Check", "Select", "Print"]

class ZeroLengthEdge(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(ZeroLengthEdge, self).__init__()
    

    def Check(self):
        allShape = self.findAllShapes()
        
        nodes = []
        for shape in allShape:
            pm.select(shape)
            pm.polySelectConstraint(m=3, t=0x8000, length=1, lb=[0, 0.000001] )
            nodes.extend( pm.ls(sl=True , flatten=True) )
            pm.polySelectConstraint(dis=True)
            pm.select(cl=True)
        return nodes
    
    def Execute(self, nodes):
        for node in nodes:
            print node
    