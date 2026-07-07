from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class DocPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout() 

        label = QLabel("Documentation")

        layout.addWidget(label)

        self.setLayout(layout)