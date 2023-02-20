# ______     ______   ______     ______     _____     ______     __         __     ______     __  __    
#/\  ___\   /\  == \ /\  ___\   /\  ___\   /\  __-.  /\  ___\   /\ \       /\ \   /\  ___\   /\ \/ /    
#\ \___  \  \ \  _-/ \ \  __\   \ \  __\   \ \ \/\ \ \ \ \____  \ \ \____  \ \ \  \ \ \____  \ \  _"-.  
# \/\_____\  \ \_\    \ \_____\  \ \_____\  \ \____-  \ \_____\  \ \_____\  \ \_\  \ \_____\  \ \_\ \_\ 
#  \/_____/   \/_/     \/_____/   \/_____/   \/____/   \/_____/   \/_____/   \/_/   \/_____/   \/_/\/_/ 
                                                                        
import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyautogui

width, height = pyautogui.size()

class Browser(QMainWindow, QWebEngineView):
    def __init__(self):
        super().__init__()

        global width, height

        self.setWindowTitle("SpeedClick Browser")

        self.setGeometry(0,0,width,height)

        self.Ui()

        self.show()

    def Ui(self):

        widget = QWidget(self)

        label = QLabel("Blerion", self)

        web = QWebEngineView()

        web.load(QUrl("https://google.com"))

        web.show()


App = QApplication(sys.argv)

window = Browser()

sys.exit(App.exec_())