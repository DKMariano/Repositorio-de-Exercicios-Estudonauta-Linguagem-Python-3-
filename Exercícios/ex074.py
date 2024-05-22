# Desafio 074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre:
# - a listagem de números gerados
# -  indique o menor e o maior valor que estão na tupla.

import random

numb = (1, 2, 3, 4, 5, 6, 7, 8, 9)
random_tup = tuple(random.sample(numb, 5))
max_tup = max(random_tup)
min_tup = min(random_tup)

# from random import randint
# print('Os valores gerados foram: ', end='')
# print(' '.join(str(item) for item in random_tup))
# print(f'O maior valor sorteado foi {max_tup}')
# print(f'O menor valor sorteado foi {min_tup}')
# from random import randint
# num = (randint(1,10), randint(1,10),  randint(1,10),  randint(1,10),  randint(1,10),  randint(1,10))
# print('Os valores sorteados foram: ', end='')
# for n in num:
# print(f'{n}', end=' ') => sem indentação
# print(f'\nO maior valor sorteado foi {max(num)}')
# print(f'O maior valor sorteado foi {min(num)}')
