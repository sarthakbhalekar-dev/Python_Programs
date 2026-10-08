import os
import sys

# macOS QtWebEngine compatibility flags
os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox --disable-gpu"

from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QToolBar,
    QLineEdit, QAction, QStyle, QLabel, QWidget, QVBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class VortexBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vortex Browser")
        self.resize(1200, 800)

        style = self.style()

        # Layout Container for Multiple Toolbars & Central View
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Tab Widget Setup
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.tab_changed)

        # Navigation Toolbar
        nav = QToolBar("Navigation")
        nav.setIconSize(QSize(18, 18))
        nav.setMovable(False)
        self.addToolBar(nav)

        # Action Buttons
        back_btn = QAction(style.standardIcon(QStyle.SP_ArrowLeft), "", self)
        back_btn.setToolTip("Back")
        back_btn.triggered.connect(lambda: self.current_browser().back() if self.current_browser() else None)
        nav.addAction(back_btn)

        next_btn = QAction(style.standardIcon(QStyle.SP_ArrowRight), "", self)
        next_btn.setToolTip("Forward")
        next_btn.triggered.connect(lambda: self.current_browser().forward() if self.current_browser() else None)
        nav.addAction(next_btn)

        reload_btn = QAction(style.standardIcon(QStyle.SP_BrowserReload), "", self)
        reload_btn.setToolTip("Reload")
        reload_btn.triggered.connect(lambda: self.current_browser().reload() if self.current_browser() else None)
        nav.addAction(reload_btn)

        home_btn = QAction(style.standardIcon(QStyle.SP_DirHomeIcon), "", self)
        home_btn.setToolTip("Home")
        home_btn.triggered.connect(self.go_home)
        nav.addAction(home_btn)

        nav.addSeparator()

        # Security Status Indicator
        self.lock_label = QLabel()
        self.lock_label.setStyleSheet("padding: 0 4px;")
        nav.addWidget(self.lock_label)

        # Address / Search Bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Search Google or type a web address...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.url_bar)

        nav.addSeparator()

        # Zoom Controls
        zoom_in_btn = QAction("+", self)
        zoom_in_btn.setToolTip("Zoom In")
        zoom_in_btn.triggered.connect(lambda: self.zoom_page(0.1))
        nav.addAction(zoom_in_btn)

        zoom_out_btn = QAction("-", self)
        zoom_out_btn.setToolTip("Zoom Out")
        zoom_out_btn.triggered.connect(lambda: self.zoom_page(-0.1))
        nav.addAction(zoom_out_btn)

        # New Tab Action
        new_tab_btn = QAction(style.standardIcon(QStyle.SP_FileDialogNewFolder), "", self)
        new_tab_btn.setToolTip("New Tab")
        new_tab_btn.triggered.connect(lambda: self.add_tab())
        nav.addAction(new_tab_btn)

        # Bookmarks Bar
        bookmarks_bar = QToolBar("Bookmarks")
        bookmarks_bar.setIconSize(QSize(14, 14))
        bookmarks_bar.setMovable(False)
        self.addToolBar(bookmarks_bar)

        bookmarks = [
            ("Google", "https://www.google.com"),
            ("YouTube", "https://www.youtube.com"),
            ("GitHub", "https://www.github.com"),
            ("Reddit", "https://www.reddit.com"),
            ("Wikipedia", "https://www.wikipedia.org"),
        ]

        for name, url in bookmarks:
            action = QAction(name, self)
            action.triggered.connect(lambda checked, target=url: self.open_bookmark(target))
            bookmarks_bar.addAction(action)

        # Attach tabs to layout
        main_layout.addWidget(self.tabs)

        # Dark Glass Modern UI Stylesheet
        self.setStyleSheet("""
            QMainWindow { background-color: #121216; }
            QToolBar {
                background-color: #1A1A22;
                border-bottom: 1px solid #282834;
                padding: 4px 8px;
                spacing: 6px;
            }
            QToolButton {
                background-color: transparent;
                color: #D1D1D6;
                border-radius: 6px;
                padding: 4px 8px;
                font-weight: 500;
                font-size: 12px;
            }
            QToolButton:hover { 
                background-color: #2A2A36; 
                color: #FFFFFF;
            }
            QLineEdit {
                background-color: #0B0B0E;
                color: #FFFFFF;
                border: 1px solid #2D2D3A;
                border-radius: 10px;
                padding: 5px 12px;
                font-size: 13px;
            }
            QLineEdit:focus { border: 1px solid #00D2FF; background-color: #14141A; }
            QTabWidget::pane { border: none; background-color: #121216; }
            QTabBar::tab {
                background-color: #1A1A22;
                color: #8E8E93;
                padding: 8px 16px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                margin-right: 4px;
                min-width: 120px;
                font-size: 12px;
            }
            QTabBar::tab:selected {
                background-color: #121216;
                color: #FFFFFF;
                border-bottom: 2px solid #00D2FF;
            }
        """)

        # Initial Tab Setup
        self.add_tab(QUrl("https://www.google.com"), "Google")

    def current_browser(self):
        return self.tabs.currentWidget()

    def add_tab(self, qurl=None, label="New Tab"):
        if not qurl or not isinstance(qurl, QUrl):
            qurl = QUrl("https://www.google.com")

        browser = QWebEngineView()
        browser.setUrl(qurl)

        index = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(index)

        # Dynamic Signals for Favicon, Title, and Address Updates
        browser.urlChanged.connect(lambda url, b=browser: self.update_urlbar(url, b))
        browser.iconChanged.connect(lambda icon, b=browser: self.update_tab_icon(icon, b))
        browser.loadFinished.connect(
            lambda _, b=browser: self.tabs.setTabText(
                self.tabs.indexOf(b), b.page().title() or "New Tab"
            ) if self.tabs.indexOf(b) != -1 else None
        )

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def tab_changed(self, index):
        browser = self.current_browser()
        if browser:
            self.update_urlbar(browser.url(), browser)

    def update_tab_icon(self, icon, browser):
        index = self.tabs.indexOf(browser)
        if index != -1:
            self.tabs.setTabIcon(index, icon)

    def update_urlbar(self, qurl, browser):
        if browser == self.current_browser():
            url_str = qurl.toString()
            self.url_bar.setText(url_str)
            if qurl.scheme() == "https":
                self.lock_label.setText("🔒")
                self.lock_label.setStyleSheet("color: #2ECC71;")
            else:
                self.lock_label.setText("🔓")
                self.lock_label.setStyleSheet("color: #F1C40F;")

    def navigate_to_url(self):
        text = self.url_bar.text().strip()
        if not text:
            return

        if "." not in text and not text.startswith("localhost"):
            text = "https://www.google.com/search?q=" + text
        elif not text.startswith("http://") and not text.startswith("https://"):
            text = "https://" + text

        if self.current_browser():
            self.current_browser().setUrl(QUrl(text))

    def open_bookmark(self, url_str):
        if self.current_browser():
            self.current_browser().setUrl(QUrl(url_str))

    def go_home(self):
        if self.current_browser():
            self.current_browser().setUrl(QUrl("https://www.google.com"))

    def zoom_page(self, delta):
        browser = self.current_browser()
        if browser:
            browser.setZoomFactor(max(0.2, browser.zoomFactor() + delta))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VortexBrowser()
    window.show()
    window.raise_()
    window.activateWindow()
    sys.exit(app.exec_())