# -*- coding:utf-8 -*-

import pymel.core as pm

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)

CLASS_NAME = "Transform"

TITLE = "Transform"
DESCRIPTION = u"디폴트 값이 아닌 트렌스폼을 검사 한다."
BUTTONS = ["Check", "Select", "Print"]

class Transform(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(Transform, self).__init__()
        self.zeroAttrs = ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"]
        self.oneAttrs = [ "scaleX", "scaleY", "scaleZ" ]
        
    def Check(self):
        allTransform = self.findAllTransforms()
        # 카메라 노드를 뺀다
        camNodes = self.findAllCamera()
        validNodes = list(set(allTransform)-set(camNodes))
        nodes = []
        
        for node in validNodes:
            for attr in self.zeroAttrs:
                value = pm.getAttr(node.name() + "." + attr)
                if value != 0:
                    nodes.append(node)
                    
            for attr in self.oneAttrs:
                value = pm.getAttr(node.name() + "." + attr)
                if value != 1:
                    nodes.append(node)   
                     
        nodes = list(set(nodes))        
        return nodes
    
    def Execute(self, nodes):
        for node in nodes:
            print "%s: T=[%d, %d, %d], R=[%d, %d, %d], S=[%d, %d, %d]"  \
            %(   node.name(), \
                 node.tx.get(), node.ty.get(), node.tz.get(), \
                 node.rx.get(), node.ry.get(), node.rz.get(), \
                 node.sx.get(), node.sy.get(), node.sz.get()
              ) 
        

    
    
        