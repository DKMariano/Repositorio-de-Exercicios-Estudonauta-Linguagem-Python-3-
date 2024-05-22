# Desafio 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex:
# - Digite um número: 1834
# Unidade: 04, Dezena 03, Centana: 08, Milhar: 01
print(' ')


num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}.')
print(f'Dezena: {d}.')
print(f'Centena: {c}.')
print(f'Milhar: {m}.')
