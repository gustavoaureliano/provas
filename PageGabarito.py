from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QPushButton, QRadioButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Estilos import Estilos
from functools import partial


class PageGabarito(QScrollArea):
    def __init__(self, parent=None):
        # Selecionar gabarito
        super().__init__(parent)
        self.setStyleSheet("border: none")
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.font = QFont()
        self.font.setPointSize(24)

        self.gabarito = []
        for n in range(90):
            self.gabarito.append("0")

        print(self.gabarito)

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

        #label alternativas
        self.frLblAlternativas = QFrame(self.page)

        self.layout_frLblAlternativas = QVBoxLayout(self.frLblAlternativas)
        self.layout.setAlignment(Qt.AlignLeft)
        self.setContentsMargins(10, 10, 10, 10)

        self.lblAlternativas = QLabel(self.frLblAlternativas)
        self.lblAlternativas.setText("Alternativas:")
        self.lblAlternativas.setFont(self.font)

        self.layout_frLblAlternativas.addWidget(self.lblAlternativas)

        #Grupos de alternativas

        self.frAlternativas = QFrame(self.page)

        self.layout_alternativas = QHBoxLayout(self.frAlternativas)
        self.layout_alternativas.setAlignment(Qt.AlignCenter)
        self.layout_alternativas.setContentsMargins(10, 10, 10, 10)

        cont = 0
        num_quests = 90
        for n in range(3):
            frGrupoAlternativas = QFrame(self.frAlternativas)

            grupoAlternativasLayout = QVBoxLayout(frGrupoAlternativas)
            grupoAlternativasLayout.setAlignment(Qt.AlignCenter)
            grupoAlternativasLayout.setContentsMargins(10, 10, 10, 10)

            for n in range(30):
                #uma alternativa
                cont += 1

                frAlternativa = QFrame(frGrupoAlternativas)

                alternativaLayout = QHBoxLayout(frAlternativa)
                alternativaLayout.setAlignment(Qt.AlignCenter)
                alternativaLayout.setContentsMargins(10, 10, 10, 10)

                numAlternativa = QLabel(frAlternativa)
                numAlternativa.setText(str(cont))
                numAlternativa.setFont(self.font)
                numAlternativa.setFixedWidth(52)
                numAlternativa.setFixedHeight(52)
                numAlternativa.setAlignment(Qt.AlignCenter)
                numAlternativa.setStyleSheet(Estilos.estiloNumAlternativa)

                alternativaLayout.addWidget(numAlternativa)

                alternativas = ["A", "B", "C", "D", "E"]

                for alt in alternativas:
                    alternativa = QPushButton(frAlternativa)
                    alternativa.setText(alt)
                    alternativa.setFont(self.font)
                    alternativa.setFixedWidth(42)
                    alternativa.setFixedHeight(42)
                    alternativa.setCursor(Qt.PointingHandCursor)
                    alternativa.setCheckable(True)
                    alternativa.setObjectName(f"alternativa{cont}{alt}")
                    alternativa.clicked.connect(partial(self.checkButton, cont, alt))
                    alternativa.setStyleSheet(Estilos.estiloBtnAlternativa)
                    alternativaLayout.addWidget(alternativa)
                grupoAlternativasLayout.addWidget(frAlternativa)
            self.layout_alternativas.addWidget(frGrupoAlternativas)

        # salvar
        self.btnSalvar = QPushButton()
        self.btnSalvar.setText("Salvar")
        self.btnSalvar.setStyleSheet(Estilos.estilobtn)

        self.btnSalvarLayout = QVBoxLayout()
        self.btnSalvarLayout.setAlignment(Qt.AlignCenter)
        self.btnSalvarLayout.setContentsMargins(10, 10, 10, 20)
        self.btnSalvarLayout.addWidget(self.btnSalvar)

        self.layout.addLayout(self.layout_num_quest)
        self.layout.addWidget(self.frLblAlternativas)
        self.layout.addWidget(self.frAlternativas)
        self.layout.addLayout(self.btnSalvarLayout)

        self.setWidget(self.page)

    def checkButton(self, i, alt):
        #print(i, alt)
        btn: QPushButton = self.frAlternativas.findChild(QPushButton, f"alternativa{i}{alt}")
        btn.setChecked(True)
        print(btn.text())
        alternativas = ["A", "B", "C", "D", "E"]
        for n in alternativas:
            if n != alt:
                opt: QPushButton = self.frAlternativas.findChild(QPushButton, f"alternativa{i}{n}")
                opt.setChecked(False)
        self.gabarito[i-1] = alt
        #print(self.gabarito)
        #if btn.isChecked():
        #    print("checked")
        #    #btn.setText("P")
        #else:
        #    print("unchecked")
        #    #btn.setText("O")
        #    #print(btn.text())
        #self.update()
        #print("checked" if btn.isChecked() else "unchecked")