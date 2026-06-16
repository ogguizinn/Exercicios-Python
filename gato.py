class Gato:
    def __init__(self,raca: str,cor:str,tipo_pelo: str,idade:int,nome:str):
    
        """
        Docstring for __init__
        
        :param self: Description
        :param raca: Digite a raça do gato
        :type raca: str
        :param cor: Digite a cor do gato
        :type cor: str
        :param tipo_pelo: Digite o tipo do pelo(Sem pelo, Pelo longo, Pelo curto)
        :type tipo_pelo: str
        :param idade: Digite a idade do gato com um número inteiro
        :type idade: int
        :param nome: Digite o nome do gato
        :type nome: str
        """
        
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.tipo_pelo = tipo_pelo
        self.idade = idade
    def miar(self):
        print(f"O {self.nome} miou")
              
meu_Gato = Gato("Persa", "Preto", "Pelo fino",7,"Guilherme")
meu_Gato.miar()