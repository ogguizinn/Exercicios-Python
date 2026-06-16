def acrescimo(preco: float , taxa: float):
    """A Função acréscimo realiza o cálculo de aumento 
    do valor do preço do produto de acordo com a taxa

    Args
        preco(float): Passe o preço do produto
        taxa(float): Passe a taxa do acréscimo somente número
    
    Returns:
        Float: Retorna o preço do produto com o valor de acréscimo
    """
# aqui o 1+ serve para duplicar o preço, pois vai fazer o preço * 1 que da o proprio preço
# então irá pegar o preço original mais o acréscimo da taxa.
    return preco * (1+(taxa) / 100)

rs = acrescimo(2560.90, 8.9)

print(f"o valor final do produto é {rs}")