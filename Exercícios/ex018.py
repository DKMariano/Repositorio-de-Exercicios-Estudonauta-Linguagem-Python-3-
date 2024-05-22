# Desafio 018
# Faça um programa que:
# - leia um ângulo qualquer
# - mostre na tela o valor do seno, cosseno e tangente do ângulo digitado

import math
a = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'Seno:  {s:.2f}.')
print(f'Cosseno: {c:.2f}.')
print(f'Tangente: {t:.2f}.')

# OU
# from math import radians, sin, cos, tan
# a = float(input('Digite um valor do ângulo: '))
# s = sin(radians(a))
# print(f'O ângulo do seno é igual a {s:.2f}.')
# c = cos(radians(a))
# print(f'O ângulo do cosseno é igual a {c:.2f}.')
# t = tan(radians(a))
# print(f'O ângulo da tangente é igual a {t:.2f}.')
