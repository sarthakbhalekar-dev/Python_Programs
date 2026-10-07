# Importing Various Important Packages
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# Starting Making The Browser
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Making The Navigation Bars
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('🠔', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('🠖', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Google', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        yt_btn = QAction("YouTube", self)
        yt_btn.triggered.connect(self.navigate_yt)
        navbar.addAction(yt_btn)

        bg_btn = QAction("WhiteBoard", self)
        bg_btn.triggered.connect(self.navigate_bg)
        navbar.addAction(bg_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    # Functions 

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_yt(self):
        self.browser.setUrl(QUrl('https://www.youtube.com'))

    def navigate_bg(self):
        self.browser.setUrl(QUrl('https://www.tutorialspoint.com/whiteboard.htm'))

       

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("RayLight's Browser")
window = MainWindow()
app.exec_()