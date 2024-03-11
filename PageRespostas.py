from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Estilos import Estilos

class PageRespostas(QScrollArea):
    def __init__(self, parent=None):
        # Selecionar gabarito
        super().__init__(parent)
        self.setStyleSheet("border: none")
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.font = QFont()
        self.font.setPointSize(24)

        self.page = QWidget(self)
        self.layout = QVBoxLayout(self.page)
        self.layout.setAlignment(Qt.AlignCenter)

        self.layout_num_quest = QHBoxLayout()
        self.layout_num_quest.setAlignment(Qt.AlignLeft)
        self.layout_num_quest.setContentsMargins(10, 10, 10, 10)

        self.lblNumQuests = QLabel(self.page)
        self.lblNumQuests.setText("Nº de questões:")
        # self.lblNumQuests.setStyleSheet("border: 1px solid red")
        self.lblNumQuests.setFont(self.font)
        self.lblNumQuests.setFixedWidth(245)

        self.leNumQuests = QLineEdit(self.page)
        self.leNumQuests.setStyleSheet("""
                QLineEdit {
                    border: 1px solid black;
                    border-radius: 5px;
                    padding: 5px;
                }
                """)
        self.leNumQuests.setFont(self.font)
        self.leNumQuests.setMaxLength(2)
        self.leNumQuests.setFixedWidth(52)
        self.leNumQuests.setFixedHeight(52)

        self.layout_num_quest.addWidget(self.lblNumQuests)
        self.layout_num_quest.addWidget(self.leNumQuests)

        # alternativas
        self.lblAlternativas = QLabel(self.page)
        self.lblAlternativas.setText("Alternativas:")
        self.lblAlternativas.setFont(self.font)

        self.layout_alternativas = QHBoxLayout()
        self.layout_alternativas.setAlignment(Qt.AlignCenter)
        self.layout_alternativas.setContentsMargins(10, 10, 10, 10)

        estibloNumAlternativa = """
                QLabel { 
                    border: 1px solid black;
                    border-radius: 26px;
                    background-color: #004040;
                    color: white;
                }
                """

        estiloBtnAlternativa = """
                    QPushButton { 
                        border: 1px solid black;
                        border-radius: 5px;
                        background-color: white;
                        color: black;
                    }
                    QPushButton:hover { 
                        border: 1px solid black;
                        border-radius: 5px;
                        background-color: #DDDFDD;
                        color: black;
                    }
                    QPushButton:pressed { 
                        border: 1px solid black;
                        border-radius: 5px;
                        background-color: #004040;
                        color: white;
                    }
                    """
        cont = 0
        num_quests = 90
        for n in range(3):
            grupoAlternativasLayout = QVBoxLayout()
            grupoAlternativasLayout.setAlignment(Qt.AlignCenter)
            grupoAlternativasLayout.setContentsMargins(10, 10, 10, 10)
            for n in range(30):
                cont += 1
                alternativaLayout = QHBoxLayout()
                alternativaLayout.setAlignment(Qt.AlignCenter)
                alternativaLayout.setContentsMargins(10, 10, 10, 10)
                numAlternativa = QLabel()
                numAlternativa.setText(str(cont))
                numAlternativa.setFont(self.font)
                numAlternativa.setFixedWidth(52)
                numAlternativa.setFixedHeight(52)
                numAlternativa.setAlignment(Qt.AlignCenter)
                numAlternativa.setStyleSheet(estibloNumAlternativa)
                alternativaLayout.addWidget(numAlternativa)
                alternativas = ["A", "B", "C", "D", "E"]
                for alt in alternativas:
                    alternativa = QPushButton()
                    alternativa.setText(alt)
                    alternativa.setFont(self.font)
                    alternativa.setFixedWidth(42)
                    alternativa.setFixedHeight(42)
                    alternativa.setCursor(Qt.PointingHandCursor)
                    alternativa.setStyleSheet(estiloBtnAlternativa)
                    alternativaLayout.addWidget(alternativa)
                grupoAlternativasLayout.addLayout(alternativaLayout)
            self.layout_alternativas.addLayout(grupoAlternativasLayout)

        # salvar
        self.btnSalvar = QPushButton()
        self.btnSalvar.setText("Salvar")
        self.btnSalvar.setStyleSheet(Estilos.estilobtn)

        self.btnSalvarLayout = QVBoxLayout()
        self.btnSalvarLayout.setAlignment(Qt.AlignCenter)
        self.btnSalvarLayout.setContentsMargins(10, 10, 10, 20)
        self.btnSalvarLayout.addWidget(self.btnSalvar)

        self.layout.addLayout(self.layout_num_quest)
        self.layout.addWidget(self.lblAlternativas)
        self.layout.addLayout(self.layout_alternativas)
        self.layout.addLayout(self.btnSalvarLayout)

        self.setWidget(self.page)