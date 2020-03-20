#!/usr/bin/env python
import os
import resources
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.utilities import logger
from qtpyvcp import actions

from tnc.widgets.designer_plugins import OpenCVPlugin

LOG = logger.getLogger('TNC.{}'.format(__name__))


class MainWindow(VCPMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.initUi()
