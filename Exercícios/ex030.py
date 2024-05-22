# Desafio 030
# Crie um programa que:
# - leia um número inteiro
# - mostre na tela se ele é par ou impar

number = int(input('Digite um número inteiro:\n'))
test = number % 2
if test == 0:
    print(f'O número {number} é par.')
else:
    print(f'O número {number} é ímpar.')
