from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QScrollArea, QPushButton, \
    QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Estilos import Estilos


class PageResultados(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("border: none")
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.correcao = dict()

        self.page = QFrame(self)
        self.layout = QVBoxLayout(self.page)
        self.layout.setAlignment(Qt.AlignTop)

        self.font = QFont()
        self.font.setPointSize(24)
        self.setFont(self.font)

        # Botão voltar

        self.frBtnVoltar = QFrame(self.page)
        # self.frBtnVoltar.setStyleSheet("border: 1px solid blue")

        self.layout_btnVoltar = QVBoxLayout(self.frBtnVoltar)
        self.layout_btnVoltar.setAlignment(Qt.AlignLeft)
        self.setContentsMargins(10, 10, 10, 10)

        self.btnVoltar = QPushButton(self.frBtnVoltar)
        self.btnVoltar.setText("Voltar")
        self.btnVoltar.setCursor(Qt.PointingHandCursor)
        self.btnVoltar.setStyleSheet(Estilos.estilobtn)

        self.layout_btnVoltar.addWidget(self.btnVoltar)

        # Resultados
        self.frResultados = QWidget(self.page)

        # Questões erradas
        self.frQuestErradas = QFrame(self.page)

        self.layout.addWidget(self.frBtnVoltar)
        self.layout.addWidget(self.frResultados)
        self.layout.addWidget(self.frQuestErradas)

        self.setWidget(self.page)

    def mostrarResultados(self):

        # self.frResultados.setStyleSheet("border: 1px solid yellow")

        self.layout_resultados = QHBoxLayout(self.frResultados)
        self.layout_resultados.setAlignment(Qt.AlignCenter)

        self.frResultadosEsquerda = QFrame(self.frResultados)

        self.layout_resultados_esquerda = QVBoxLayout(self.frResultadosEsquerda)
        self.lblTotal = QLabel("Total de questões:", self.frResultadosEsquerda)
        self.lblTotal.setFont(self.font)
        self.lblTotal.setAlignment(Qt.AlignRight)
        self.lblAcertos = QLabel("Acertos:", self.frResultadosEsquerda)
        self.lblAcertos.setFont(self.font)
        self.lblAcertos.setAlignment(Qt.AlignRight)
        self.lblErros = QLabel("Erros:", self.frResultadosEsquerda)
        self.lblErros.setFont(self.font)
        self.lblErros.setAlignment(Qt.AlignRight)

        self.layout_resultados_esquerda.addWidget(self.lblTotal)
        self.layout_resultados_esquerda.addWidget(self.lblAcertos)
        self.layout_resultados_esquerda.addWidget(self.lblErros)

        self.frResultadosDireita = QFrame(self.frResultados)

        self.layout_resultados_direita = QVBoxLayout(self.frResultadosDireita)

        self.numTotal = QLabel(self.frResultadosDireita)
        total = self.correcao["total"]
        self.numTotal.setText(str(total))
        self.numTotal.setFont(self.font)

        self.numAcertos = QLabel(self.frResultadosDireita)
        acertos = self.correcao["acertos"]
        porcentagemAcertos = (acertos / total) * 100
        self.numAcertos.setText(f"{acertos}/{total} ({porcentagemAcertos:.1f}%)")
        self.numAcertos.setFont(self.font)

        self.numErros = QLabel(self.frResultadosDireita)
        erros = self.correcao["erros"]
        porcentagemErros = (erros / total) * 100
        self.numErros.setText(f"{erros}/{total} ({porcentagemErros:.1f}%)")
        self.numErros.setFont(self.font)

        self.layout_resultados_direita.addWidget(self.numTotal)
        self.layout_resultados_direita.addWidget(self.numAcertos)
        self.layout_resultados_direita.addWidget(self.numErros)

        self.layout_resultados.addWidget(self.frResultadosEsquerda)
        self.layout_resultados.addWidget(self.frResultadosDireita)

        # Questões erradas
        self.frQuestErradas.setStyleSheet("border: 1px solid pink")
        self.frQuestErradas.setFont(self.font)

        self.layout_quest_erradas = QGridLayout(self.frQuestErradas)
        self.layout_quest_erradas.setAlignment(Qt.AlignCenter)
        self.layout_quest_erradas.setContentsMargins(10, 10, 10, 10)

        #self.frLblQuestErradas = QFrame(self.frQuestErradas)
        #self.frLblQuestErradas.setStyleSheet("border: 1px solid purple")

        #self.layoutLblQuestErradas = QVBoxLayout(self.frLblQuestErradas)
        #self.layoutLblQuestErradas.setContentsMargins(10, 10, 10, 10)

        #self.lblQuestErradas = QLabel(self.frLblQuestErradas)
        #self.lblQuestErradas.setText("Questões Erradas")
        #self.lblQuestErradas.setFont(self.font)
        #self.layoutLblQuestErradas.addWidget(self.lblQuestErradas)

        #self.layout_quest_erradas.addWidget(self.frLblQuestErradas, 0, 1, 0, 1)

        frNumQuests = QFrame(self.frQuestErradas)

        layout_num_quests = QVBoxLayout(frNumQuests)
        layout_num_quests.setAlignment(Qt.AlignCenter)
        layout_num_quests.setContentsMargins(10, 10, 10, 10)

        frEscolhida = QFrame(self.frQuestErradas)

        layout_escolhida = QVBoxLayout(frEscolhida)
        layout_escolhida.setAlignment(Qt.AlignCenter)
        layout_escolhida.setContentsMargins(10, 10, 10, 10)

        frCorreta = QFrame(self.frQuestErradas)

        layout_correta = QVBoxLayout(frCorreta)
        layout_correta.setAlignment(Qt.AlignCenter)
        layout_correta.setContentsMargins(10, 10, 10, 10)

        numQuest = QLabel(frNumQuests)
        numQuest.setText("Nº")
        numQuest.setFont(self.font)
        numQuest.setStyleSheet("border: 1px solid lime")
        layout_num_quests.addWidget(numQuest)

        lblEscolhida = QLabel(frEscolhida)
        lblEscolhida.setText("Escolhida")
        lblEscolhida.setFont(self.font)
        lblEscolhida.setStyleSheet("border: 1px solid lime")
        layout_escolhida.addWidget(lblEscolhida)

        lblCorreta = QLabel(frCorreta)
        lblCorreta.setText("Correta")
        lblCorreta.setFont(self.font)
        lblCorreta.setStyleSheet("border: 1px solid lime")
        layout_correta.addWidget(lblCorreta)

        self.layout_quest_erradas.addWidget(frNumQuests, 1, 0)
        self.layout_quest_erradas.addWidget(frEscolhida, 1, 1)
        self.layout_quest_erradas.addWidget(frCorreta, 1, 2)

        erradas = self.correcao["erradas"]
        print("Erradas:", erradas)

        for i, (num, escolhida, correta) in enumerate(erradas):
            # print(i, num, escolhida, correta)
            if (num, escolhida, correta) not in self.correcao["sem_responder"]:
                frNumQuests = QFrame(self.frQuestErradas)

                layout_num_quests = QVBoxLayout(frNumQuests)
                layout_num_quests.setAlignment(Qt.AlignCenter)
                layout_num_quests.setContentsMargins(10, 10, 10, 10)

                frEscolhida = QFrame(self.frQuestErradas)

                layout_escolhida = QVBoxLayout(frEscolhida)
                layout_escolhida.setAlignment(Qt.AlignCenter)
                layout_escolhida.setContentsMargins(10, 10, 10, 10)

                frCorreta = QFrame(self.frQuestErradas)

                layout_correta = QVBoxLayout(frCorreta)
                layout_correta.setAlignment(Qt.AlignCenter)
                layout_correta.setContentsMargins(10, 10, 10, 10)

                numQuest = QLabel(self.frQuestErradas)
                numQuest.setText(f"{num:0>2}")
                numQuest.setFont(self.font)
                numQuest.setFixedSize(52, 52)
                numQuest.setStyleSheet(Estilos.estiloNumAlternativa)

                lblEscolhida = QLabel(self.frQuestErradas)
                lblEscolhida.setText(escolhida)
                lblEscolhida.setFont(self.font)
                lblEscolhida.setFixedSize(42, 42)
                lblEscolhida.setStyleSheet(Estilos.estiloAlternativa)
                lblEscolhida.setAlignment(Qt.AlignCenter)

                lblCorreta = QLabel(self.frQuestErradas)
                lblCorreta.setText(correta)
                lblCorreta.setFont(self.font)
                lblCorreta.setFixedSize(42, 42)
                lblCorreta.setStyleSheet(Estilos.estiloAlternativa)
                lblCorreta.setAlignment(Qt.AlignCenter)

                layout_num_quests.addWidget(numQuest)
                layout_escolhida.addWidget(lblEscolhida)
                layout_correta.addWidget(lblCorreta)

                self.layout_quest_erradas.addWidget(frNumQuests, i + 2, 0)
                self.layout_quest_erradas.addWidget(frEscolhida, i + 2, 1)
                self.layout_quest_erradas.addWidget(frCorreta, i + 2, 2)
        # self.layout_quest_erradas.addLayout(self.layout_num_quests)
        # self.layout_quest_erradas.addLayout(self.layout_escolhida)
        # self.layout_quest_erradas.addLayout(self.layout_correta)
