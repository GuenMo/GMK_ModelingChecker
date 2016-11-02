# -*- coding:utf-8 -*-

import pymel.core as pm

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

CLASS_NAME = "LockTransform"

TITLE = "Lock Transform"
DESCRIPTION = u"잠긴 어트리뷰트가 있는지 검사 합니다."
BUTTONS = ["Check", "Select", "Unlock"]

class LockTransform(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(LockTransform, self).__init__()
    
    def Check(self):
        allTransform = self.findAllTransforms()
        # 카메라 노드를 뺀다
        camNodes = self.findAllCamera()
        validNodes = list(set(allTransform)-set(camNodes))
        nodes = []
        
        for node in validNodes:
            nodes.extend(node.listAttr(locked=True))
        
        return nodes
    
    def Select(self, nodes):
        return self.Select_tramsformFromAttr(nodes)
    
    def Execute(self, nodes):
        for attr in nodes:
            pm.setAttr(attr, lock=False)
        

    
    
        