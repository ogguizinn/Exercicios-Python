from PyQt6.QtWidgets import QApplication, QWidget,QLabel,QLineEdit,QTableWidget, QVBoxLayout,QHBoxLayout 
from PyQt6.QtGui import QPixmap
from sys import argv  

class Caixa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(150,50,1600,900)

        #Criar o layout horizontal 
        self.layout_horizontal = QHBoxLayout()
        #Vamos criar as duas colunas = Esquerda e direita 
        self.label_col_esquerda = QLabel()
        #Alterar a cor de fundo da label esquerda
        self.label_col_esquerda.setStyleSheet("QLabel {background-color:#FFFFFF}")
        self.label_col_esquerda.setFixedWidth(800)    
        

        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel {background-color:#000000}")
            



        #Criar o layout dos elementos da coluna da esquerda. Este layout é vertical 
        self.layout_vert_col_esq= QVBoxLayout()

        #Vamos criar uma label para adicionar o logo da padaria 
        self.label_logo = QLabel()
        #Vamos setar o pixmap a label para carregar a imagem 
        self.label_logo.setPixmap(QPixmap("img/logo.png"))
        #ajustar a imagem a label 
        self.label_logo.setScaledContents(True)

        #criar a label do codigo do produto
        self.label_cod_produto = QLabel("Código do Produto")
        self.label_cod_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt; color: #8F0A0A}")
        self.edit_cod_produto = QLineEdit()
        self.edit_cod_produto.setStyleSheet("QLineEdit(font-size:15pt)")

        #criar a label e o edit do nome do produto ----------------------
        self.label_nome_produto = QLabel("Nome do Produto")
        self.label_nome_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt; color: #8F0A0A}")
        self.edit_nome_produto = QLineEdit()
        self.edit_nome_produto.setStyleSheet("QLineEdit(font-size:15pt)")

        #criar a label e o edit da descrição do produto ----------------------
        self.label_descricao_produto = QLabel("descricao do Produto")
        self.label_descricao_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt; color: #8F0A0A}")
        self.edit_descricao_produto = QLineEdit()
        self.edit_descricao_produto.setStyleSheet("QLineEdit(font-size:15pt)")
        self.edit_descricao_produto.setFixedHeight(88)


        #criar a label da Quantidade do produto
        self.label_quantidade_produto = QLabel("Quantidade do Produto")
        self.label_quantidade_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt; color: #8F0A0A}")
        self.edit_quantidade_produto = QLineEdit()
        self.edit_quantidade_produto.setStyleSheet("QLineEdit(font-size:15pt)")

        #criar a label do Preço Unitário do produto
        self.label_Precounitario_produto = QLabel("Preco Unitario do Produto")
        self.label_Precounitario_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt; color: #8F0A0A}")
        self.edit_Precounitario_produto = QLineEdit()
        self.edit_Precounitario_produto.setStyleSheet("QLineEdit(font-size:15pt)")

        #criar a label do Sub Total do produto
        self.label_SubTotal_produto = QLabel("Sub Total do Produto")
        self.label_SubTotal_produto.setStyleSheet("QLabel{font-weight:bold;font-size:15pt; color: #8F0A0A}")
        self.edit_SubTotal_produto = QLineEdit()
        self.edit_SubTotal_produto.setStyleSheet("QLineEdit(font-size:15pt)")

        


        # adicionar o logo ao layout vertical
        self.layout_vert_col_esq.addWidget(self.label_logo)
        #adicionar o código do produto
        self.layout_vert_col_esq.addWidget(self.label_cod_produto)
        self.layout_vert_col_esq.addWidget(self.edit_cod_produto)
        
         #adicionar o nome do produto
        self.layout_vert_col_esq.addWidget(self.label_nome_produto)
        self.layout_vert_col_esq.addWidget(self.edit_nome_produto)

        #adicionar a descrição do produto

        self.layout_vert_col_esq.addWidget(self.label_descricao_produto)
        self.layout_vert_col_esq.addWidget(self.edit_descricao_produto)
        self.edit_descricao_produto.setStyleSheet("QLabel{font-weigh:bold; font-size:15pt; color:#ffffff}")
        self.edit_descricao_produto = QLineEdit()
        self.edit_descricao_produto.setStyleSheet("QLineEdit{font-size:15pt}")

        #adicionar a Quantidade do produto
        self.layout_vert_col_esq.addWidget(self.label_quantidade_produto)
        self.layout_vert_col_esq.addWidget(self.edit_quantidade_produto)

        #adicionar o Preço Unitário do produto
        self.layout_vert_col_esq.addWidget(self.label_Precounitario_produto)
        self.layout_vert_col_esq.addWidget(self.edit_Precounitario_produto)

        #adicionar o Sub Total do produto
        self.layout_vert_col_esq.addWidget(self.label_SubTotal_produto)
        self.layout_vert_col_esq.addWidget(self.edit_SubTotal_produto)
        


        
        
        #setar o layout vertical a label coluna esquerda 
        self.label_col_esquerda.setLayout(self.layout_vert_col_esq)


        






































        #Adicionar as colunas esquerda e direita ao layout horizontal 
        self.layout_horizontal.addWidget(self.label_col_esquerda)
        self.layout_horizontal.addWidget(self.label_col_direita)

        #Setar o layout horizontal a nossa janela 
        self.setLayout(self.layout_horizontal)



app = QApplication(argv)
janela=Caixa()
janela.show()
app.exec()
        