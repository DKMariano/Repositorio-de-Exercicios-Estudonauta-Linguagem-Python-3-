# Desafio 013:
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
f = input('Qual o nome do funcionário? ')
s1 = float(input(f'Qual é o salário antigo de {f}? '))
a = s1 * 0.15
s2 = s1 + a
print(' ')
print('-' * 40)
print(f"{'CALCULADORA DE SALÁRIO':^40}")
print('_' * 40)
print(f'Nome do funcionário: {f}')
print(f'Salário antigo: R$ {s1:.2f}')
print(f'Salário atual: R$ {s2:.2f}')
print(f'Total do aumento: R$ {a:.2f}')
