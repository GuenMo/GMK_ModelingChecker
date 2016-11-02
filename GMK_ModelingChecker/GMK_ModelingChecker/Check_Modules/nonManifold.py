# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)
import pymel.core as pm


CLASS_NAME = "NonManifold"

TITLE = "Non Manifold"
DESCRIPTION = u"비 정상적으로 연결이 된 엣지를 검사 합니다."
BUTTONS = ["Check", "Select", "Print"]

class NonManifold(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(NonManifold, self).__init__()
    
        
    def Check(self):
        allShape = self.findAllShapes()
        
        nodes = []
        for shape in allShape:
            nonMainfold = pm.polyInfo(shape, nme=True)
            if nonMainfold != None:
                nodes.extend( nonMainfold )
        return nodes
    
    def Execute(self, nodes):
        for node in nodes:
            print node
    