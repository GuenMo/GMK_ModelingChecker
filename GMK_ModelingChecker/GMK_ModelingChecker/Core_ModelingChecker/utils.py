# -*- coding:utf-8 -*-

import maya.OpenMayaUI as OMUI
from shiboken import wrapInstance
from PySide.QtCore import * 
from PySide.QtGui import *
import collections
import pymel.core as pm
from datetime import datetime

def getMayaWindow():
    ptr = OMUI.MQtUtil.mainWindow()
    return wrapInstance(long(ptr), QMainWindow)

def getRootPath():
    utilsPath = __file__.replace("\\", "/")
    rootPath = utilsPath.rpartition("/")[0].rpartition("/")[0]
    return rootPath

def getIconPath():
    return getRootPath() + "/Icons_ModelingChecker/" 


def findAllModuel(relativeDirectory):
    # relativeDirectory 경로에 모든 모듈(.py)를 검색해 리턴한다.
    allPyFiles = findAllFile( relativeDirectory, ".pyc" )
    returnModules = []
    
    for f in allPyFiles:
        if f != "__init__":
            returnModules.append(f)

    return returnModules

def findAllFile(relativeDirectory, fileExtension):
    # 주어진 확장자를 가지는 모든 파일을 찾아서 리턴 한다.
    import os
    
    fileDirectory = getRootPath()  + relativeDirectory + "/"
    allFiles = os.listdir(fileDirectory)
    returnFiles = []
    
    for f in allFiles:
        splitString = str(f).rpartition(fileExtension)
        if not splitString[1] == "" and splitString[2] == "":
            returnFiles.append(splitString[0])
        
    return returnFiles

def list_duplicates(seq):
    tally = collections.defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() if len(locs)>1)

def versionCheck():
    currentVersion = pm.versions.current()
    
    if '2014' in str(currentVersion): 
        return True
    elif '2016' in str(currentVersion): 
        return True
    else:
        return False    
    
def dateCheck():
    limitsDate = datetime(2015,12,31)
    currentDate = datetime.now()
    
    if currentDate <  limitsDate:
        return True
    else:
        return False
        
def checkSystem():
    #verStat = versionCheck()
    dateStat = dateCheck()
    
    if dateStat:
        return True
    else:
        return False
    
    
    
    
    
    