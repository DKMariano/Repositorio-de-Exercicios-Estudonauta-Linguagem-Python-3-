# Desafio 12:
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


print(' ')
print('-' * 40)
print('CALCULADORA DE DESCONTOS'.center(40))
print('_' * 40)
print(' ')
p = float(input('Digite o preço do produto: R$ '))
d = 0.05 * p
t = p - d
print(' ')
print('-' * 40)
print(f'Valor do produto: R$ {p:.2f}')
print(f'Valor do desconto: R$ {d:.2f}')
print(f'Total a pagar: R$ {t:.2f}')
print('_' * 40)
