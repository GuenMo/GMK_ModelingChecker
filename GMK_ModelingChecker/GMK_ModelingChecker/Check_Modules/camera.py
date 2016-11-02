# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

CLASS_NAME = "Camera"

TITLE = "Camera"
DESCRIPTION = u"커스텀 카메라가 있는지 검사 합니다."
BUTTONS = ["Check", "Select", "Delete"]

class Camera(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(Camera, self).__init__()
        self.defaultCamSetting()
    
    def Check(self):
        nodes = self.findCustomCamera()
        return nodes
    
        

    
    
            