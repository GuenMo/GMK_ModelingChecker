import Core_ModelingChecker.checkBase as checkBase
reload(checkBase)
import pymel.core as pm

CLASS_NAME = 'TriangleFace'
TITLE = 'Triangle Face'
DESCRIPTION = u'\uc0bc\uac01\ud615\uc758 \uba74\uc774 \uc788\ub294\uc9c0 \uac80\uc0ac\ud569\ub2c8\ub2e4.'
BUTTONS = ['Check', 'Select', 'Print']

class TriangleFace(checkBase.CheckBase):

    def __init__(self):
        self.moduleName = CLASS_NAME
        super(TriangleFace, self).__init__()

    def Check(self):
        allShape = self.findAllShapes()
        nodes = []
        for shape in allShape:
            pm.select(shape)
            pm.polySelectConstraint(m=3, t=8, sz=1)
            nodes.extend(pm.ls(sl=True, flatten=True))
            pm.polySelectConstraint(dis=True)
            pm.select(cl=True)

        return nodes

    def Execute(self, nodes):
        for node in nodes:
            print node