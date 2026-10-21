
import sys
from urllib.parse import quote_plus

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget,
    QToolBar, QLineEdit, QAction, QLabel
)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class VortexBrowser(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vortex Browser")
        self.resize(1200, 800)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setDocumentMode(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_address)

        self.setCentralWidget(self.tabs)

        # Navigation bar
        toolbar = QToolBar("Navigation")
        self.addToolBar(toolbar)

        self.add_button(toolbar, "←", self.go_back)
        self.add_button(toolbar, "→", self.go_forward)
        self.add_button(toolbar, "⟳", self.reload_page)
        self.add_button(toolbar, "⌂", self.go_home)

        self.security_label = QLabel("  ")
        toolbar.addWidget(self.security_label)

        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText(
            "Search Google or enter a website..."
        )
        self.address_bar.returnPressed.connect(self.navigate)
        toolbar.addWidget(self.address_bar)

        self.add_button(toolbar, "+", self.new_tab)
        self.add_button(toolbar, "−", self.zoom_out)
        self.add_button(toolbar, "Zoom +", self.zoom_in)

        # Bookmarks
        bookmarks = QToolBar("Bookmarks")
        self.addToolBar(bookmarks)

        websites = {
            "Google": "https://www.google.com",
            "YouTube": "https://www.youtube.com",
            "GitHub": "https://github.com",
            "Wikipedia": "https://www.wikipedia.org"
        }

        for name, url in websites.items():
            action = QAction(name, self)
            action.triggered.connect(
                lambda checked=False, link=url: self.open_url(link)
            )
            bookmarks.addAction(action)

        # Keyboard shortcuts
        self.add_shortcut("Ctrl+T", self.new_tab)
        self.add_shortcut("Ctrl+W", self.close_current_tab)
        self.add_shortcut("Ctrl+L", self.address_bar.setFocus)
        self.add_shortcut("Ctrl+R", self.reload_page)

        # Dark theme
        self.setStyleSheet("""
            QMainWindow {
                background: #15151c;
            }

            QToolBar {
                background: #20202b;
                border: none;
                padding: 6px;
                spacing: 6px;
            }

            QToolButton {
                color: white;
                background: #30303d;
                padding: 6px;
                border-radius: 5px;
            }

            QToolButton:hover {
                background: #45455a;
            }

            QLineEdit {
                background: #101018;
                color: white;
                border: 1px solid #45455a;
                border-radius: 8px;
                padding: 8px;
            }

            QTabWidget::pane {
                border: none;
            }

            QTabBar::tab {
                background: #282835;
                color: #cccccc;
                padding: 9px 18px;
            }

            QTabBar::tab:selected {
                background: #45455a;
                color: white;
            }
        """)

        self.new_tab()

    def add_button(self, toolbar, name, function):
        action = QAction(name, self)
        action.triggered.connect(function)
        toolbar.addAction(action)

    def add_shortcut(self, shortcut, function):
        action = QAction(self)
        action.setShortcut(shortcut)
        action.triggered.connect(function)
        self.addAction(action)

    def current_browser(self):
        return self.tabs.currentWidget()

    def new_tab(self):
        browser = QWebEngineView()

        index = self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentIndex(index)

        browser.urlChanged.connect(
            lambda url, b=browser: self.update_url(url, b)
        )

        browser.titleChanged.connect(
            lambda title, b=browser: self.update_title(title, b)
        )

        browser.setUrl(QUrl("https://www.google.com"))

    def update_title(self, title, browser):
        index = self.tabs.indexOf(browser)

        if index != -1:
            self.tabs.setTabText(index, title[:20] or "New Tab")

    def update_url(self, url, browser):
        if browser == self.current_browser():
            self.address_bar.setText(url.toString())

            if url.scheme() == "https":
                self.security_label.setText("🔒")
            else:
                self.security_label.setText("")

    def update_address(self, index):
        browser = self.current_browser()

        if browser:
            self.update_url(browser.url(), browser)

    def navigate(self):
        text = self.address_bar.text().strip()

        if not text:
            return

        if text.startswith(("http://", "https://")):
            url = text

        elif " " not in text and (
            "." in text or text.startswith("localhost")
        ):
            url = "https://" + text

        else:
            url = (
                "https://www.google.com/search?q="
                + quote_plus(text)
            )

        self.open_url(url)

    def open_url(self, url):
        browser = self.current_browser()

        if browser:
            browser.setUrl(QUrl(url))

    def go_back(self):
        browser = self.current_browser()
        if browser:
            browser.back()

    def go_forward(self):
        browser = self.current_browser()
        if browser:
            browser.forward()

    def reload_page(self):
        browser = self.current_browser()
        if browser:
            browser.reload()

    def go_home(self):
        self.open_url("https://www.google.com")

    def zoom_in(self):
        browser = self.current_browser()
        if browser:
            zoom = min(browser.zoomFactor() + 0.1, 3.0)
            browser.setZoomFactor(zoom)

    def zoom_out(self):
        browser = self.current_browser()
        if browser:
            zoom = max(browser.zoomFactor() - 0.1, 0.5)
            browser.setZoomFactor(zoom)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            widget = self.tabs.widget(index)
            self.tabs.removeTab(index)
            widget.deleteLater()

    def close_current_tab(self):
        self.close_tab(self.tabs.currentIndex())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = VortexBrowser()
    window.show()

    sys.exit(app.exec_())
