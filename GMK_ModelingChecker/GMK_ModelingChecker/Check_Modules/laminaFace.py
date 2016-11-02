# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)
import pymel.core as pm


CLASS_NAME = "LaminaFace"

TITLE = "Lamina Face"
DESCRIPTION = u"겹쳐진 면을 찾습니다."
BUTTONS = ["Check", "Select", "Print"]

class LaminaFace(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(LaminaFace, self).__init__()
    

    def Check(self):
        allShape = self.findAllShapes()
        
        nodes = []
        for shape in allShape:
            faces = pm.ls(pm.polyInfo(shape, lf=True), flatten=True)
            nodes.extend( faces )
        return nodes
    
    def Execute(self, nodes):
        print TITLE
        for node in nodes:
            print node
    