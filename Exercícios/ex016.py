# Desafio 016
# Crie um programa que:
# - leia um número real qualquer digitado
# - mostre na tela a sua porção inteira.
# Ex: Ao digitar o numero 6.127 o programa deve mostrar 6 como parte inteira.

import math
n = float(input('Digite um número real: '))
r = math.trunc(n)
print(f'A parte inteira de {n} é {r}.')

# print(f'A parte inteira de {n} é {math.trunc(n)}.')
# OU
# from math import trunc
# n = float(input('Digite um número real: '))
# print(f'A parte inteira de {n} é {trunc(n)}.')
# OU
# n = float(input('Digite um número real: '))
# print(f'A parte inteira de {n} é {int(n)}.')
