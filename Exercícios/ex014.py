# Desafio 014:
# Escreva um programa que converta a temperatura digitada de ºC para ºF

print(' ')
print('-' * 40)
print(f"{'CONVERSOR DE TEMPERATURA':^40}")
print('_' * 40)
print(' ')
c = float(input('Qual é a temperatura atual em ºC? '))
f = (c * 1.8) + 32
k = c + 273.15
print(' ')
print('-' * 40)
print(f'Temperatura em Fahrenheit: {f:.2f}ºF')
print(f'Temperatura em Kelvin    : {k:.2f}ºK')
print('_' * 40)
