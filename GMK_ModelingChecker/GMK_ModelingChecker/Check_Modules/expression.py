# -*- coding:utf-8 -*-

import pymel.core as pm

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

CLASS_NAME = "Expression"

TITLE = "Expression"
DESCRIPTION = u"expression 노드가 있는지 검사를 합니다."
BUTTONS = ["Check", "Select", "Delete"]

class Expression(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(Expression, self).__init__()
    
    def Check(self):
        nodes = pm.ls(type = "expression")

        return nodes

    def Select(self, nodes):
        return self.Select_dwStrimNode(nodes)
    
        