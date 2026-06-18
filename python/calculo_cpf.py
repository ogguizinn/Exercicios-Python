# Pedir ao usuário a entrada dos números do cpf e guarda na variável
#cpf_original. Aqui o usuário digitará o cpf completo

cpf_original = input ("Digite o seu CPF apenas números:")
#ajuda a contar os números do cpf no laço while
i = 0

#guarda os 9 primeiros digitos do cpf
cpf_9 = ""

#Enquanto(while) o valor de 1 for menor que 9, neste caso, irá até 8
#vai pegando um número por vez no cpf_original(digitado elo usuario com
# 11 digitos) e vai adicionado, um ao lado do outro, na variável cpf_9.
# A ideia é obter os 9 primeiros digitos 
while i < 9:
    cpf_9+=cpf_original[i]
    i+=1
print (cpf_9)

#para calcular o primeiro digito verificador, iremos usar cada número do 
# cpf_9 multiplicado pelo peso que vai de 10 a 2
peso = 10

# A variável resultado é utilizada para guarda a soma do resultado da 
#multiplicação


resultado = 10

# Variável i usada par aobter um número por vez do cpf_9

i = 0
while i < 10:



#A variável resultado soma os resultados obtidos da multiplicação
#dos números do cpf com o peso. Como a variável cpf_9 é uma cadeia
#de string. será necessário converter cada número obtido para inteiro
#com o comando int
    resultado+=int(cpf_9[i]) * peso
    # Peso -= 1, diminuir em 1 o valor do peso, passando de 10 para 9, depois 
    #para 8 e assim por diante até chegar em 2
    peso-=1

    # A variável i, que inicia com 0, deve ser incrementada em 1(i+=1) para
    # sair de zero(0) e chegar em 8. Assim a cada vez que o laço roda(executa)
    # o valor de i é incrementado em 1, então ele, i, vai para 1 depois 2 
    # e assim por diante até chegar em 9(sendo 9 o ponto de saída)
    i+=1
    print(resultado)

    # A variável resto guarda o resultado do cálculo entre o resultado, que
    #foi obtido dentro do laço while com o número 11. Nesta operação estamos
    #obtendo o resto da divisão, por isso, usamos o operado %.
    #se o resto da divisão for menor que 2, então o primeiro digito
    #verificador é zero (0). Note que ele está entre aspas, pois queremos
    #juntar coms os outros números que estão dentro da variável cpf_9, que
    #também são caracteres
    # caso o resultado do cálculo resulte em número maior que 2, então faz-se
    # a subtração de 11 por resto, que é o resultado do cálculo. Para manter
    # o valor em formato string, estamos usando o comando str(string)
resto = resultado % 11 
if resto < 2:
   cpf_9 +="0"

else:
    cpf_9 += str(11-resto)
    print(cpf_9)

if cpf_9 == cpf_original:
    print ("CPF Válido!")
else:
    print("CPF Inválido!")

