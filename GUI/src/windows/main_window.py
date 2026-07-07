from PySide6.QtWidgets import  ( 
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
    )

from pages.home_page import HomePage
from pages.docs_page import DocPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Engineering Calculator")
        self.resize(1840, 960)

        # ---------- Central Widget ----------
        central = QWidget()
        self.setCentralWidget(central)

        # ---------- Main Layout ----------
        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        # ---------- Sidebar ----------
        sidebar_layout = QVBoxLayout()

        home_button = QPushButton("Home")
        doc_button = QPushButton("Documents")

        sidebar_layout.addWidget(home_button)
        sidebar_layout.addWidget(doc_button)
        sidebar_layout.addStretch()

        # ---------- Pages ----------
        self.stack = QStackedWidget() 

        self.home_page = HomePage()
        self.docs_page = DocPage()

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.docs_page)

        # Show Home first
        self.stack.setCurrentWidget(self.home_page)

        # ---------- Navigation ----------
        home_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.home_page)
        )

        doc_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.docs_page)
        )

        # ---------- Assemble ----------
        main_layout.addLayout(sidebar_layout, 1)
        main_layout.addWidget(self.stack, 4)

        

