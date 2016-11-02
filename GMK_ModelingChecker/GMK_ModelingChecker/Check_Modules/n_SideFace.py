# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)
import pymel.core as pm


CLASS_NAME = "NSideFace"

TITLE = "N Side Face"
DESCRIPTION = u"다각형의 면이 있는지 검사합니다."
BUTTONS = ["Check", "Select", "Print"]

class NSideFace(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(NSideFace, self).__init__()
    
        
    def Check(self):
        allShape = self.findAllShapes()
        
        nodes = []
        for shape in allShape:
            pm.select(shape)
            pm.polySelectConstraint(m=3, t=8, sz=3)
            nodes.extend( pm.ls(sl=True , flatten=True) )
            pm.polySelectConstraint(dis=True)
            pm.select(cl=True)
        return nodes
    
    def Execute(self, nodes):
        for node in nodes:
            print node
    