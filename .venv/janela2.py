from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys
class janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha janela")
        # A largura, altura e posição da janela 
        self.setGeometry(10,20,800,400)

app = QApplication(sys.argv)
tela = janela2()
tela.show()
app.exec()
