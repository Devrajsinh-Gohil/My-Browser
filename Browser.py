# Import The Required Libraries
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


# Create The Main Window
class MainWindow(QMainWindow):

    # Constructor
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Create QWebEngineView
        self.browser = QWebEngineView()

        # Set Default Browser URL
        self.browser.setUrl(QUrl("http://google.com"))

        # Add Action When The URL Is Changed
        self.browser.urlChanged.connect(self.update_urlbar)

        # Add Action When The Loading Is Finished
        self.browser.loadFinished.connect(self.update_title)

        # Set Browser As Main Window
        self.setCentralWidget(self.browser)

        # Create A Status Bar
        self.status = QStatusBar()

        # Add status Bar To The Main Window
        self.setStatusBar(self.status)

        # Create QToolBar For Navigation
        navtb = QToolBar("Navigation")

        # Add Tool Bar To The Main Window
        self.addToolBar(navtb)

        # Add Actions To The Tool Bar

        # Create Back
        back_btn = QAction("Back", self)

        # Set Status Tip
        back_btn.setStatusTip("Back to previous page")

        # Add Action To The Back Button

        # Go Back
        back_btn.triggered.connect(self.browser.back)

        # Add To Tool Bar
        navtb.addAction(back_btn)

        # Create Forward
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")

        # Add Action To The Next Button

        # Go Forward
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        # Create Reload
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")

        # Add Action To The Reload Button

        # Browser Reload
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # Home Button
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # Separator
        navtb.addSeparator()

        # Line Edit For The URL
        self.urlbar = QLineEdit()

        # Return Key
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # Add To The Tool Bar
        navtb.addWidget(self.urlbar)

        # Add Stop
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")

        # Add Action To The Stop Button
        # Browser Stop
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)

        # Show
        self.show()

    # Update The Title Of The Window
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Devraj" % title)

    # Home Action
    def navigate_home(self):
        # Open Google
        self.browser.setUrl(QUrl("http://www.google.com"))

    # Line Edit
    def navigate_to_url(self):
        # Get URL
        q = QUrl(self.urlbar.text())

        # If Blank
        if q.scheme() == "":
            # Set To
            q.setScheme("http")

        # Set URL
        self.browser.setUrl(q)

    # Update URL
    def update_urlbar(self, q):
        # Set Text
        self.urlbar.setText(q.toString())

        # Set Cursor Position
        self.urlbar.setCursorPosition(0)


# Create Application
app = QApplication(sys.argv)

# Setting Name
app.setApplicationName("My Browser")

# Create Window Object
window = MainWindow()

# Loop
app.exec_()
