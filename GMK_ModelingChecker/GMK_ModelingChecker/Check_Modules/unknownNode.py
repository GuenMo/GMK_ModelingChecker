# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)
import pymel.core as pm


CLASS_NAME = "UnknownNode"

TITLE = "Unknown Node"
DESCRIPTION = u"알수 없는 노드를 검사 합니다."
BUTTONS = ["Check", "Select", "Delete"]

class UnknownNode(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(UnknownNode, self).__init__()
        self.nodeType = ["unknown"]
        
    def Check(self):
        nodes = pm.ls(type = self.nodeType)
        return nodes
    
    def Execute(self, nodes):
        for node in nodes:
            pm.lockNode(node, lock=False)
        
        pm.delete(nodes)