# -*- coding:utf-8 -*-

import pymel.core as pm

class CheckBase(object):
    def __init__(self):
        self.selectionClear()
        
    # module function
    def Check(self):
        pass
    
    def Select(self, nodes):
        # 반드시 리턴 값이 있어야 한다
        pm.select(nodes, r=True)
        sels = pm.ls(sl=True)
        return sels
    
    def Execute(self, nodes):
        pm.delete(nodes)
    
    #====================================================
    # built-in function
    def selectionClear(self):
        pm.select(cl=True)
        
    def findAllShapes(self): 
        nodes = pm.ls(type = ["mesh", "nurbsSurface", "subdiv", 'nurbsCurve'])
        return nodes
    
    def findAllTransforms(self):
        nodes = pm.ls(type= "transform")
        return nodes
    
    # camera
    def findAllCamera(self):
        camShapes = pm.ls(type = "camera")
        camTrnasforms = []
        
        for shape in camShapes:
            camTrnasforms.append(shape.getParent())
        
        camShapes.extend(camTrnasforms)
        return camShapes
    
    def findDefaultCamera(self):
        camNames = ['front', 'persp', 'side', 'top']
        camNodes = []
        
        for cam in camNames:
            camNodes.append(pm.PyNode(cam))
        
        return camNodes 
    
    def findCustomCamera(self):
        camNodes = self.findAllCamera()
        names = ['frontShape', 'perspShape', 'sideShape', 'topShape', 'front', 'persp', 'side', 'top']
        defaultCamNodes = []
        
        for n in names:
            defaultCamNodes.append(pm.PyNode(n))
        
        nodes = list(set(camNodes) - set(defaultCamNodes))
        return nodes
    
    def defaultCamSetting(self):
        cams = self.findDefaultCamera()
        for cam in cams:
            cam.visibility.set(False)
        
    # Select Type
    def Select_dwStrimNode(self, nodes):
        connectedNodes = []
        
        for node in nodes:
            attrs = node.outputs(plugs=True)
            for attr in attrs:
                connectedNodes.append(attr.node())
        
        returnNode = list(set(connectedNodes))
        pm.select(returnNode, nodes, r=True)
        return pm.ls(sl=True)
    
    def Select_upStrimNode(self, nodes):
        connectedNodes = []
        
        for node in nodes:
            attrs = node.inputs(plugs=True)
            for attr in attrs:
                connectedNodes.append(attr.node())
        
        returnNode = list(set(connectedNodes))
        pm.select(returnNode, nodes, r=True)
        
        return pm.ls(sl=True)
    
    def Select_tramsformFromShape(self, nodes):
        transformNodes = []
        
        for n in nodes:
            transformNodes.append(n.getParent())
        
        pm.select(transformNodes, nodes, r=True)
        return pm.ls(sl=True)
    
    def Select_tramsformFromAttr(self, nodes):
        transformNodes = []
        
        for n in nodes:
            transformNodes.append(n.node())
        transformNodes = list(set(transformNodes))
        pm.select(transformNodes, nodes, r=True)
        return pm.ls(sl=True)
    
    
    
    
    