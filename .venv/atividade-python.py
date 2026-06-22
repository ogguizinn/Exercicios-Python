from PyQt6.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QTableWidget, QVBoxLayout,QHBoxLayout,QTableWidgetItem 
from PyQt6.QtGui import QPixmap,QIcon
from sys import argv  
from os import system
from PyQt6.QtCore import Qt


class Pagina(QWidget):

    def __init__(self):
        self.linha= 0 
        self.valor_total = 0.0

    def cadastrar(self):
        nome = self.edit_nome_pessoa.text()
        email = self.edit_nome_email.text()
        senha = self.edit_add_senha.text()

        print("Nome:", nome)
        print("Email:", email)
        print("Senha:", senha)

        super().__init__()
        self.setWindowTitle("Página de Acesso")
        self.setGeometry(150,50,1600,900)

        self.setWindowIcon(QIcon("scooby.png"))

        # =============================================================== CRIAÇÃO LAYOUTS ======================================================================================
        # Criar o layout horizontal ---------------------------------------------------------------------------------------
        self.layout_horizontal = QHBoxLayout()


        # Vamos criar as duas colunas: Esquerda e Direita
        # e alterar as cores de fundo de cada uma:

        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:#FC6F00}")

        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:#FC6F00}")
        self.label_col_esquerda.setFixedWidth(800)

        # ========================================================== LADO ESQUERDO TELA ========================================================================================
        # Criar o layout dos elementos da coluna da esquerda. Este layout é vertical --------------------------------------------------------------------------------------
        self.layout_vert_col_esq = QVBoxLayout()


        # vamos criar uma label para adicionar o logo 
        self.label_logo = QLabel()
        # Vamos setar o Pixmap à label para carregar a imagem
        self.label_logo.setPixmap(QPixmap("cachorrinho.png"))
        # Ajustar a imagem à label
        self.label_logo.setScaledContents(True)

         # criar a label de colocar seu nome ----------------------------------------------------------------------------------
        self.label_nome_pessoa = QLabel("Digite seu Nome")
        self.label_nome_pessoa.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.edit_nome_pessoa = QLineEdit()
        self.edit_nome_pessoa.setStyleSheet("QLineEdit{font-size:18pt}")


        # criar a label digitacao Do email ----------------------------------------------------------------------------------
        self.label_nome_email = QLabel("Insira o seu Email")
        self.label_nome_email.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.edit_nome_email = QLineEdit()
        self.edit_nome_email.setStyleSheet("QLineEdit{font-size:18pt}")

        # criar a label adicionar a senha ----------------------------------------------------------------------------------
        self.label_add_senha = QLabel("Escolha sua senha")
        self.label_add_senha.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.label_add_senha = QLineEdit()
        self.label_add_senha.setStyleSheet("QLineEdit{font-size:18pt}")

        # criar a label Cadastrar  ----------------------------------------------------------------------------------
        self.label_cadastro = QLabel("CADASTRAR")
        self.label_cadastro.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        self.label_cadastro = QLineEdit()
        self.label_cadastro.setStyleSheet("QLineEdit{font-size:18pt}")



        # Adicionando os elementos do lado da esquerda --------------------------------------------------------------------------------------------------------
        
        # Adicionar o logo ao layout vertical
        self.layout_vert_col_esq.addWidget(self.label_logo)

        # Adicionar o Nome da pessoa
        self.layout_vert_col_esq.addWidget(self.label_nome_pessoa)
        self.layout_vert_col_esq.addWidget(self.edit_nome_pessoa)

        # Adicionar o email da pessoa
        self.layout_vert_col_esq.addWidget(self.label_nome_email)
        self.layout_vert_col_esq.addWidget(self.edit_nome_email)

        # Adicionar a senha do user
    
        self.label_add_senha = QLabel("Escolha sua senha")
        self.label_add_senha.setStyleSheet("QLabel {font-weight:bold; font-size:15pt; color:#ffffff}")
        
        # Campo de senha
        self.edit_add_senha = QLineEdit()
        self.edit_add_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.edit_add_senha.setStyleSheet("QLineEdit{font-size:18pt}")

        self.layout_vert_col_esq.addWidget(self.label_add_senha)
        self.layout_vert_col_esq.addWidget(self.edit_add_senha)

        # Campo Cadastrar
        self.layout_vert_col_esq.addWidget(self.label_cadastro)
        self.layout_vert_col_esq.addWidget(self.label_cadastro)









         # Setar o layout vertical à label lado da esquerda
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)

        # ================================================================ FIM LADO ESQUERDO ===============================================================================





app = QApplication(argv)
janela = Pagina()
janela.show()
app.exec()





































