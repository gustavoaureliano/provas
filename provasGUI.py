import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QScrollArea, QStackedWidget, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PageHome import PageHome
from PageGabarito import PageGabarito
from Header import Header
from PageRespostas import PageRespostas
from PageResultados import PageResultados
import provas

class Janela(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.largura = 1180
        self.altura = 620
        self.titulo = "Provas"
        self.gabarito = []
        self.respostas = []

        for n in range(90):
            self.gabarito.append("0")
            self.respostas.append("0")

        self._centralWidget = QWidget()
        self._centralWidget.setStyleSheet("background-color: white")
        self._centralWidget.setContentsMargins(0, 0, 0, 0)

        self.layout = QVBoxLayout(self._centralWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        #self.layout.setAlignment(Qt.AlignCenter)

        #Header
        self.header = Header(self._centralWidget)

        #Páginas
        self.paginas = QStackedWidget(self._centralWidget)

        #Página Home
        self.home_page = PageHome(self.paginas)
        self.home_page.btnGabarito.clicked.connect(self.selecionarGabarito)
        self.home_page.btnRespostas.clicked.connect(self.selecionarRespostas)
        self.home_page.btnCorrigir.clicked.connect(self.corrigir)
        self.paginas.addWidget(self.home_page)

        #Página gabarito
        self.gabarito_page = PageGabarito(self.paginas)
        self.gabarito_page.btnSalvar.clicked.connect(self.salvarGabarito)
        self.paginas.addWidget(self.gabarito_page)

        #Página Respostas
        self.respostas_page = PageGabarito(self.paginas)
        self.respostas_page.btnSalvar.clicked.connect(self.salvarRespostas)
        self.paginas.addWidget(self.respostas_page)

        # Página correção
        self.resultados_page = PageResultados(self.paginas)
        self.resultados_page.btnVoltar.clicked.connect(self.voltarHome)
        self.paginas.addWidget(self.resultados_page)

        #Página principal
        self.paginas.setCurrentWidget(self.home_page)
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.paginas)

        self.setCentralWidget(self._centralWidget)
        self.resize(self.largura, self.altura)
        self.setWindowTitle(self.titulo)

    def voltarHome(self):
        self.paginas.setCurrentWidget(self.home_page)

    def selecionarGabarito(self):
        self.gabarito_page.gabarito = self.gabarito
        self.paginas.setCurrentWidget(self.gabarito_page)

    def selecionarRespostas(self):
        self.paginas.setCurrentWidget(self.respostas_page)

    def salvarGabarito(self):
        self.gabarito = self.gabarito_page.gabarito
        self.voltarHome()
        #file = open("gabarito.txt", mode="w")
        #gabarito = self.gabarito_page.gabarito
        #save = ""
        #for quest, alt in gabarito.items():
        #    save += f"{quest}: {alt}\n"
        #file.write(save)
        #file.close()

    def salvarRespostas(self):
        self.respostas = self.respostas_page.gabarito
        self.voltarHome()

    def corrigir(self):
        self.resultados_page = PageResultados(self.paginas)
        self.resultados_page.btnVoltar.clicked.connect(self.voltarHome)
        self.paginas.addWidget(self.resultados_page)
        correcao = provas.corrigir(self.gabarito, self.respostas)
        print("Gabatito:", self.gabarito)
        print("Respostas:", self.respostas)
        print(correcao)
        self.resultados_page.correcao = correcao
        self.resultados_page.mostrarResultados()
        self.paginas.setCurrentWidget(self.resultados_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela()
    window.show()
    sys.exit(app.exec())
