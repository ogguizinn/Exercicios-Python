# Importação de funções especificas de módulos, usamos o from para indicar de onde
# vem a função, o import para indicar quais funções irão ser usadas.
from os import system, cpu_count
from math import sqrt, pow, pi

system("cls")
print("===== Origem OS =====")
print(cpu_count())

print("==== Origem Math =====")
print(sqrt(49))
print(pow(2,5))