# Desafio 089
# Crie um programa que leia nome e duas notas de vários alunos, guardando-os em uma lista composta.
# No final, mostre um boletim contendo a média de cada um.
# Permita também que o usuário possa mostrar as notas de cada aluno individualmente.

print('-=' * 30)
print(f"{'CADASTRO DE ALUNOS DA ESCOLA GUANABARA':^60}")
print('-=' * 30)
print('')

student_list = list()
temporary_list = list()

while True:
    name = input('Nome: ')
    temporary_list.append(name)
    grade1 = float(input('Nota da 1ª Avaliação: '))
    temporary_list.append(grade1)
    grade2 = float(input('Nota da 2ª Avaliação: '))
    temporary_list.append(grade2)
    average = (grade1 + grade2) / 2
    temporary_list.append(round(average, 1))
    student_list.append(temporary_list[:])
    temporary_list.clear()
    flag = input("Deseja continuar? ")
    if flag in "Nn":
        break

print('')
print('-' * 30)
print(f"{'BOLETIM':^30}")
print('-' * 30)

print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 30)

for number in range(len(student_list)):
    print(f'{number:<4}{student_list[number][0]:<10}{student_list[number][3]:>8.1f}')

print('')
while True:
    student = int(input('Você deseja exibir a nota de qual aluno? (999 terminar o programa): \n'))
    if student != 999:
        print('-' * 30)
        print(f'As nota de {student_list[student][0]} foram: ')
        print(f'1º Avaliação: {student_list[student][1]}')
        print(f'2º Avaliação: {student_list[student][2]}')
        print('-' * 30)
        print('')
    if student == 999:
        break
print('')
print('-' * 30)
print('Obrigado por usar o nosso programa.')
print('Tenha um bom dia!!')
print('-' * 30)
print('')
