def desconto(preco=0.0, taxa=0.0):
    """A Função Desconto calcula o valor 
    de desconto de um determinado preço"""
    return preco * taxa / 100

rs = desconto(100, 4.2)
print(f"O Valor do desconto é {rs}")