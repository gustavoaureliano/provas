from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Estilos import Estilos

class PageHome(QWidget):
    def __init__(self, parent=None):
        # Home
        super().__init__(parent)
        self.setStyleSheet("background-color: white")
        self.home_layout = QVBoxLayout(self)
        self.home_layout.setAlignment(Qt.AlignCenter)

        # botões home

        # Botões das questões
        self.layout_btn_quests = QHBoxLayout()
        self.layout_btn_quests.setAlignment(Qt.AlignVCenter)
        self.fontLblBtn = QFont()
        self.fontLblBtn.setPointSize(11)

        # Botão gabarito

        self.btnGabarito_layout = QVBoxLayout()
        self.btnGabarito_layout.setAlignment(Qt.AlignHCenter)
        self.btnGabarito_layout.setContentsMargins(30, 30, 30, 30)

        self.btnGabarito = QPushButton(self)
        self.btnGabarito.setText("Selecionar \ngabarito")
        self.btnGabarito.setCursor(Qt.PointingHandCursor)
        self.btnGabarito.setStyleSheet(Estilos.estilobtn)

        self.lblGabarito = QLabel(self)
        self.lblGabarito.setText("Gabarito não selecionado")
        self.lblGabarito.setFont(self.fontLblBtn)
        self.lblGabarito.setStyleSheet("color: black;")
        self.lblGabarito.setAlignment(Qt.AlignCenter)

        self.btnGabarito_layout.addWidget(self.btnGabarito)
        self.btnGabarito_layout.addWidget(self.lblGabarito)

        self.layout_btn_quests.addLayout(self.btnGabarito_layout)

        # Botão respostas
        self.btnRespostas_layout = QVBoxLayout()
        self.btnRespostas_layout.setAlignment(Qt.AlignHCenter)
        self.btnRespostas_layout.setContentsMargins(30, 30, 30, 30)

        self.btnRespostas = QPushButton(self)
        self.btnRespostas.setText("Selecionar \nrespostas")
        self.btnRespostas.setCursor(Qt.PointingHandCursor)
        self.btnRespostas.setStyleSheet(Estilos.estilobtn)

        self.lblRespostas = QLabel(self)
        self.lblRespostas.setText("Respostas não selecionadas")
        self.lblRespostas.setFont(self.fontLblBtn)
        self.lblRespostas.setStyleSheet("color: black;")
        self.lblRespostas.setAlignment(Qt.AlignCenter)

        self.btnRespostas_layout.addWidget(self.btnRespostas)
        self.btnRespostas_layout.addWidget(self.lblRespostas)

        self.layout_btn_quests.addLayout(self.btnRespostas_layout)

        # Botão da correção
        self.layout_btn_correcao = QVBoxLayout()
        self.layout_btn_correcao.setAlignment(Qt.AlignVCenter)
        self.layout_btn_correcao.setContentsMargins(50, 30, 50, 30)

        self.btnCorrigir = QPushButton(self)
        self.btnCorrigir.setText("Corrigir")
        self.btnCorrigir.setCursor(Qt.PointingHandCursor)
        self.btnCorrigir.setStyleSheet(Estilos.estilobtn)

        self.layout_btn_correcao.addWidget(self.btnCorrigir)

        self.home_layout.addLayout(self.layout_btn_quests)
        self.home_layout.addLayout(self.layout_btn_correcao)