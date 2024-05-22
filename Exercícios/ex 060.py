# Desafio 060
# Faça um programa que:
# - leia um número qualquer
# - mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.

num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print(f'{num}! = ', end='')
for c in range(1,num + 1 ):
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}', end='')


# num = int(input('Digite um número para calcular seu fatorial: '))
# c = num
# f = 1
# print(f'{num}! = ', end='')
# while c > 0:
    # print(f'{c}', end='')
    # print(' x 'if c > 1 else ' = ', end='')
    # f *= c
    # c -= 1
# print(f'{f}', end='')

# from math import factorial
# num = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(num)
# print(f'O fatorial de {num} é {f}.')
