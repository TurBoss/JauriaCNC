from qtpyvcp.widgets.qtdesigner import _DesignerPlugin
from computer_vision.opencv_widget import OpenCVWidget


class OpenCVPlugin(_DesignerPlugin):
    def pluginClass(self):
        return OpenCVWidget
