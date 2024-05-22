# Desafio 034
# Escreva um programa que:
# - pergunte o salário de um funcionário
# - calcule e mostre na tela o valor do seu aumento
# Para salários superiores a R$1250,00:
# - o aumento de 10%.
# Para os inferiores ou iguais:
# - o aumento é de 15%.

name = input('Qual o nome do funcionário? ').upper()
salary = float(input(f'Qual é o salário antigo de {name}? '))
if salary <= 1250:
    new_salary = salary * 1.15
else:
    new_salary = salary * 1.10
increase = new_salary - salary
print(' ')
print('-=-' * 40)
print('CALCULADORA DE SALÁRIO'.center(40))
print('-=-' * 40)
print(f'Nome do funcionário: {name}')
print(f'Salário antigo: R$ {salary:.2f}')
print(f'Salário atual: R$ {new_salary:.2f}')
print(f'Total do aumento: R$ {increase:.2f}')
