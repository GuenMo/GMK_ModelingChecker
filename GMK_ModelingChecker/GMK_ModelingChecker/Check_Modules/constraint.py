# -*- coding:utf-8 -*-

import pymel.core as pm

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

CLASS_NAME = "Constraint"

TITLE = "Constraint"
DESCRIPTION = u"컨스트인 노드가 있는 검사 합니다."
BUTTONS = ["Check", "Select", "Delete"]

class Constraint(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(Constraint, self).__init__()
    
    def Check(self):
        nodes = pm.ls(type = ["parentConstraint", "orientConstraint", "pointConstraint", "aimConstraint"])
        return nodes
    
    def Select(self, nodes):
        self.Select_tramsformFromShape(nodes)