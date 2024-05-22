# Desafio 090
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.


name = input('Nome: ')
grade = float(input(f'Média de {name}: '))
student = {'Nome': name, 'Média': grade}

print('-=' * 30)

for k, v in student.items():
    print(f'{k} é {v}.')
if student['Média'] >= 7:
    print('A situação é igual a APROVADO!')
elif student['Média'] >= 5:
    print('A situação é igual a RECUPERAÇÃO!')
else:
    print('A situação é igual a REPROVADO!')
