# -*- coding:utf-8 -*-

import pymel.core as pm

import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)
import collections
import Core_ModelingChecker.utils as utils
reload(utils)


CLASS_NAME = "NameConflict"

TITLE = "Name Conflict"
DESCRIPTION = u"같은 이름의 오브젝트가 있는지 검사를 합니다."
BUTTONS = ["Check", "Select", "Print"]

class NameConflict(checkBase.CheckBase):
    def __init__(self):
        self.moduleName = CLASS_NAME
        super(NameConflict, self).__init__()
    
    def Check(self):
        nodes = []

        allNodes = pm.ls(dag=True)#, transforms=True)
        nodeNames = []
        for node in allNodes:
            nodeNames.append( node.name().rpartition("|")[2] )
        
        namesForSurch = [x for x, y in collections.Counter(nodeNames).items() if y > 1]
        
        sameNameNodes = []
        if len(namesForSurch) != 0:
            for item in utils.list_duplicates(nodeNames):
                sameNameNodes.append(item)
        
        indexes = []
        for value in sameNameNodes:
            indexes.extend(value[1])
        for i in indexes:
            nodes.append(allNodes[i])
            
        return nodes
    
    def Execute(self, nodes):
        for node in nodes:
            print node.name()
    