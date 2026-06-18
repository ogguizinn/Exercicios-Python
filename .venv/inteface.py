from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QGridLayout, QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
import sys


class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Vendas")
        self.resize(900, 600)

        layout_principal = QVBoxLayout()

        # =================== LOGO ===================
        logo = QLabel()
        pixmap = QPixmap("logoo.png")  # Coloque sua logo nesta pasta
        logo.setPixmap(pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo = QLabel("SISTEMA DE VENDAS")
        titulo.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(logo)
        layout_principal.addWidget(titulo)

        # =================== CAMPOS ===================
        grid = QGridLayout()

        self.edit_codigo = QLineEdit()
        self.edit_nome = QLineEdit()
        self.edit_descricao = QLineEdit()
        self.edit_quantidade = QLineEdit()
        self.edit_preco = QLineEdit()
        self.edit_subtotal = QLineEdit()

        self.edit_subtotal.setReadOnly(True)

        grid.addWidget(QLabel("Código do Produto"), 0, 0)
        grid.addWidget(self.edit_codigo, 0, 1)

        grid.addWidget(QLabel("Nome do Produto"), 0, 2)
        grid.addWidget(self.edit_nome, 0, 3)

        grid.addWidget(QLabel("Descrição"), 1, 0)
        grid.addWidget(self.edit_descricao, 1, 1, 1, 3)

        grid.addWidget(QLabel("Quantidade"), 2, 0)
        grid.addWidget(self.edit_quantidade, 2, 1)

        grid.addWidget(QLabel("Preço Unitário"), 2, 2)
        grid.addWidget(self.edit_preco, 2, 3)

        grid.addWidget(QLabel("Subtotal"), 3, 0)
        grid.addWidget(self.edit_subtotal, 3, 1)

        layout_principal.addLayout(grid)

        # =================== BOTÕES ===================
        botoes = QHBoxLayout()

        btn_adicionar = QPushButton("Adicionar Produto")
        btn_adicionar.clicked.connect(self.adicionar_produto)

        botoes.addStretch()
        botoes.addWidget(btn_adicionar)

        layout_principal.addLayout(botoes)

        # =================== TABELA ===================
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)

        self.tabela.setHorizontalHeaderLabels([
            "Código",
            "Nome",
            "Descrição",
            "Quantidade",
            "Preço",
            "Subtotal"
        ])

        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setDefaultSectionSize(130)

        layout_principal.addWidget(self.tabela)

        self.setLayout(layout_principal)

    def adicionar_produto(self):
        linha = self.tabela.rowCount()
        self.tabela.insertRow(linha)

        codigo = self.edit_codigo.text()
        nome = self.edit_nome.text()
        descricao = self.edit_descricao.text()

        quantidade = int(self.edit_quantidade.text())
        preco = float(self.edit_preco.text().replace(",", "."))

        subtotal = quantidade * preco

        self.edit_subtotal.setText(f"{subtotal:.2f}")

        self.tabela.setItem(linha, 0, QTableWidgetItem(codigo))
        self.tabela.setItem(linha, 1, QTableWidgetItem(nome))
        self.tabela.setItem(linha, 2, QTableWidgetItem(descricao))
        self.tabela.setItem(linha, 3, QTableWidgetItem(str(quantidade)))
        self.tabela.setItem(linha, 4, QTableWidgetItem(f"{preco:.2f}"))
        self.tabela.setItem(linha, 5, QTableWidgetItem(f"{subtotal:.2f}"))


app = QApplication(sys.argv)
janela = Janela()
janela.show()
sys.exit(app.exec())