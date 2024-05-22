# Desafio 040:
# Crie um programa que:
# - leia duas notas de um aluno
# - calcule sua média
# - mostre uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

name = input('Digite o nome do estudante:\n').upper()
first_grade = float(input('Digite a primeira nota do aluno:\n'))
second_grade = float(input('Digite a primeira nota do aluno:\n'))
final_grade = (first_grade + second_grade) / 2
print(' ')
print('-'*40)
print('CALCULADORA DE NOTAS'.center(40))
print('_'*40)
print(f'Aluno(a): {name}')
print(f'Nota da primeira avaliação: {first_grade:.1f}')
print(f'Nota da segunda avaliação: {second_grade:.1f}')
print(f'Média: {final_grade:.1f}')
if first_grade < 5.0:
    print(f'\033[1;31m {name} NÃO ATINGIU a nota mínima para aprovação.\033[m')
elif final_grade >= 7.0:
    print(f'\033[1;32m{name} ATINGIU a nota mínima para aprovação.\033[m ')
else:
    print(f'\033[1;33m {name} está em RECUPERAÇÃO.\033[m ')
print('_'*40)
