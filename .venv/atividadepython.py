from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)
from PyQt6.QtGui import QPixmap, QIcon
from sys import argv


class Pagina(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Página Voluntariedade")
        self.setGeometry(150, 50, 1600, 900)

        self.setStyleSheet("background-color:#323A4B")

        self.setWindowIcon(QIcon("petshop.png"))

        # ================= Layout Principal =================

        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.setSpacing(0)

        # ================= Coluna Esquerda =================

        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet(
            "background-color:#FC6F00;"
        )
        self.label_col_esquerda.setFixedWidth(800)

        self.layout_vert_col_esq = QVBoxLayout()

        self.label_logo = QLabel()
        self.label_logo.setPixmap(QPixmap("petshop.png"))
        self.label_logo.setScaledContents(True)

        self.layout_vert_col_esq.addWidget(self.label_logo)

        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)

        # ================= Coluna Direita =================

        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet(
            "background-color:#FC6F00;"
        )

        self.layout_vert_col_dir = QVBoxLayout()

        self.label_voluntario = QLabel(
            "Seja Voluntário, seja empático!"
        )
        self.label_voluntario.setStyleSheet("""
            font-size:25pt;
            font-weight:bold;
            color:#000000;
        """)

        self.label_aumigo = QLabel(
            "Ajude nossos animaizinhos encontrar um Aumigo e encontrar um lar, tenha empatinha!"
        )
        self.label_aumigo.setStyleSheet("""
            font-size:14pt;
            color:black;
        """)

        self.label_seunome = QLabel("Seu Nome:")
        self.label_seunome.setStyleSheet("font-size:15pt;color:black;")

        self.edit_seunome = QLineEdit()
        self.edit_seunome.setFixedHeight(50)

        self.label_seuemail = QLabel("Seu Email:")
        self.label_seuemail.setStyleSheet("font-size:15pt;color:black;")

        self.edit_seuemail = QLineEdit()
        self.edit_seuemail.setFixedHeight(50)

        self.label_suasenha = QLabel("Sua Senha:")
        self.label_suasenha.setStyleSheet("font-size:15pt;color:black;")

        self.edit_suasenha = QLineEdit()
        self.edit_suasenha.setEchoMode(QLineEdit.EchoMode.Password)
        self.edit_suasenha.setFixedHeight(50)

        # ================= Botões =================

        self.button_cadastrar = QPushButton("Cadastre-se")
        self.button_cadastrar.setStyleSheet("""
            QPushButton{
                background:#323A4B;
                color:white;
                font-size:15px;
                border-radius:8px;
            }

            QPushButton:hover{
                background:#44526B;
            }
        """)
        self.button_cadastrar.setFixedHeight(50)
        self.button_cadastrar.clicked.connect(self.cadastrar)

        self.button_cadastrargoogle = QPushButton(
            "Cadastrar com Google"
        )
        self.button_cadastrargoogle.setStyleSheet("""
            QPushButton{
                background:#FA4E3E;
                color:white;
                font-size:15px;
                border-radius:8px;
            }
        """)
        self.button_cadastrargoogle.setFixedHeight(50)
        self.button_cadastrargoogle.clicked.connect(
            self.cadastrar_google
        )

        self.button_cadastrarfacebook = QPushButton(
            "Cadastrar com Facebook"
        )
        self.button_cadastrarfacebook.setStyleSheet("""
            QPushButton{
                background:#23599B;
                color:white;
                font-size:15px;
                border-radius:8px;
            }
        """)
        self.button_cadastrarfacebook.setFixedHeight(50)
        self.button_cadastrarfacebook.clicked.connect(
            self.cadastrar_facebook
        )

        # ================= Adicionando Widgets =================

        self.layout_vert_col_dir.addWidget(self.label_voluntario)
        self.layout_vert_col_dir.addWidget(self.label_aumigo)

        self.layout_vert_col_dir.addWidget(self.label_seunome)
        self.layout_vert_col_dir.addWidget(self.edit_seunome)

        self.layout_vert_col_dir.addWidget(self.label_seuemail)
        self.layout_vert_col_dir.addWidget(self.edit_seuemail)

        self.layout_vert_col_dir.addWidget(self.label_suasenha)
        self.layout_vert_col_dir.addWidget(self.edit_suasenha)

        self.layout_vert_col_dir.addSpacing(15)

        self.layout_vert_col_dir.addWidget(self.button_cadastrar)
        self.layout_vert_col_dir.addWidget(self.button_cadastrargoogle)
        self.layout_vert_col_dir.addWidget(self.button_cadastrarfacebook)

        self.label_col_direita.setLayout(self.layout_vert_col_dir)

        # ================= Layout Principal =================

        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)

        self.setLayout(self.layout_horizontal)

    # ============================================================

    def cadastrar(self):

        nome = self.edit_seunome.text()
        email = self.edit_seuemail.text()
        senha = self.edit_suasenha.text()

        if nome == "" or email == "" or senha == "":
            QMessageBox.warning(
                self,
                "Aviso",
                "Preencha todos os campos!"
            )
            return

        QMessageBox.information(
            self,
            "Sucesso",
            f"Cadastro realizado!\n\nNome: {nome}\nEmail: {email}"
        )

        self.edit_seunome.clear()
        self.edit_seuemail.clear()
        self.edit_suasenha.clear()

    # ============================================================

    def cadastrar_google(self):
        QMessageBox.information(
            self,
            "Google",
            "Funcionalidade em desenvolvimento com DEV Guilherme."
        )

    # ============================================================

    def cadastrar_facebook(self):
        QMessageBox.information(
            self,
            "Facebook",
            "Funcionalidade em desenvolvimento com DEV Guilherme."
        )


# ============================================================

if __name__ == "__main__":
    app = QApplication(argv)

    janela = Pagina()
    janela.show()

    app.exec()