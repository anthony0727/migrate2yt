from PyQt5.QtWidgets import QMainWindow

# from PyQt5 import uic
# Ui_MainWindow = uic.loadUiType("/Users/anthony/repo/myyoutubemusic/app/views/MainWindow_ui.ui")[0]
#
# # TODO: deploy - conver .ui files into .py files
from .MainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
