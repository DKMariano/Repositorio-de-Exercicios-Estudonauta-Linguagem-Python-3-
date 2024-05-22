# Desafio 017
# Faça um programa que:
# - leia o comprimento do cateto oposto
# - leia o comprimento do cateto adjacente
# - calcule e mostre o comprimento da hipotenusa

import math
cop = float(input('Digite o comprimento do cateto oposto: '))
cad = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(cop, cad)
print(f'O comprimento da hipotenusa é igual a {hip:.2f}.')

# OU
# cop = float(input('Digite o comprimento do cateto oposto: '))
# cad = float(input('Digite o comprimento do cateto adjacente: '))
# hip = (co ** 2 + ca ** 2) ** (1/2)
# print(f'O comprimento da hipotenusa é igual a {hip:.2f}.')

# OU
# from math import hypot
# cop = float(input('Digite o comprimento do cateto oposto: '))
# cad = float(input('Digite o comprimento do cateto adjacente: '))
# hip = hypot(cop, cad)
# print(f'O comprimento da hipotenusa é igual a {hip:.2f}.')
