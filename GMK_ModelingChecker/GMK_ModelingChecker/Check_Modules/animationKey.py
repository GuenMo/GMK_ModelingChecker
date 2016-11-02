# -*- coding:utf-8 -*-

import pymel.core as pm

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

CLASS_NAME = "AnimationKey"

TITLE = "Animation Key"
DESCRIPTION = u"애니메이션 키가 있는지 검사를 합니다."
BUTTONS = ["Check", "Select", "Delete"]

class AnimationKey(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(AnimationKey, self).__init__()
    
    def Check(self):
        nodes = pm.ls(type = ["animCurveTL", "animCurveTA", "animCurveTT", "animCurveTU", "animCurveUL", "animCurveUA", "animCurveUT", "animCurveUU"])
        return nodes
    
    def Select(self, nodes):
        return self.Select_dwStrimNode(nodes)
        

    
    
        