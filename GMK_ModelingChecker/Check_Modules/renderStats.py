# -*- coding:utf-8 -*-

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

import pymel.core as pm

CLASS_NAME = "RenderStats"

TITLE = "Render Stats"
DESCRIPTION = u"쉐입에 렌더 스테이트가 디폴트인지 검사 합니다."
BUTTONS = ["Check", "Select", "Reset"]

class RenderStats(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(RenderStats, self).__init__()
        
        self.attrs = ["castsShadows", "receiveShadows", "motionBlur", "primaryVisibility", "smoothShading", "visibleInReflections", "visibleInRefractions", "doubleSided"]
        
        
    def Check(self):
        allShape = self.findAllShapes()
        
        nodes = []
        for shape in allShape:
            for attr in self.attrs:
                value = pm.getAttr(shape.name() + "." + attr)
                if not value:
                    nodes.append(shape)   
        nodes = list(set(nodes))
        return nodes
    
    def Select(self, nodes):
        return self.Select_tramsformFromShape(nodes)
    
    def Execute(self, nodes):
        for node in nodes:
            for attr in self.attrs:
                pm.setAttr(node.name() + "." + attr, True)
        