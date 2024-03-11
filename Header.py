from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Header(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("QFrame { background-color: #004040; }")
        #self.setFixedHeight(60)

        self.font = QFont()
        self.font.setPointSize(24)

        self.lblHeader = QLabel(self)
        self.lblHeader.setText("Corrigir provas")
        self.lblHeader.setStyleSheet("QLabel { color: white; }")
        self.lblHeader.setFont(self.font)
        self.lblHeader.setAlignment(Qt.AlignCenter)

        self.header_layout = QVBoxLayout()
        self.header_layout.setAlignment(Qt.AlignCenter)
        self.header_layout.addWidget(self.lblHeader)

        self.setLayout(self.header_layout)
