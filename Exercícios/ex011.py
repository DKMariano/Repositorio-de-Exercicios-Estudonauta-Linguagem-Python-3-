# Desafio 011
# Faça um programa que:
# - leia a largura e a altura em metros.
# - Calcule sua área e a quantidade de tinta necessária para pintá-la.
# Sabe-se que cada litro de tinta consegue pintar uma área de 2m²

l1 = float(input('Qual a largura da parede em metros? '))
h = float(input('Qual a altura da parede em metros? '))
a = l1 * h
t = a / 2
print('-' * 40)
print('MEDIDOR DE TINTA'.center(40))
print('_' * 40)
print(' ')
print(f'Dimensão da parede: {l1} m x {h} m')
print(f'Área da parede: {a} m²')
print(f'A quantidade de tinta: {t:.2f}l.')
