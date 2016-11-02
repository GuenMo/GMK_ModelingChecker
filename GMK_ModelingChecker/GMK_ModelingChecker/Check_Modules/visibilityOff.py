# -*- coding:utf-8 -*-

import pymel.core as pm

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

CLASS_NAME = "VisibilityOff"

TITLE = "Visibility Off"
DESCRIPTION = u"비져블이 꺼져있는 오브젝트를 검사 합니다."
BUTTONS = ["Check", "Select", "Visible"]

class VisibilityOff(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(VisibilityOff, self).__init__()
    
    def Check(self):
        inVisibileNodes = pm.ls(type= "transform", invisible=True)
        defaultCamNodes = self.findDefaultCamera()
        
        nodes = list(set(inVisibileNodes) - set(defaultCamNodes))
        return nodes
    
    def Execute(self, nodes):
        for node in nodes:
            node.visibility.set(True)
        

    
    
        