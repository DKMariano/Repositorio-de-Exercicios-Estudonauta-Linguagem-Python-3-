# Desafio 086
# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))

print('=-' * 30)

for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}]', end='')
    print('')

# list1 = [[], [], []]
# list2 = [[], [], []]
# list3 = [[], [], []]
# number_list = [list1, list2, list3]
# for position in range(len(list1)):
    # numb = int(input(f'Digite um valor para [0, {position}]: '))
    # list1[position].append(numb)

# for position in range(len(list2)):
#    numb = int(input(f'Digite um valor para [1, {position}]: '))
#    list2[position].append(numb)

# for position in range(len(list3)):
#    numb = int(input(f'Digite um valor para [2, {position}]: '))
#    list3[position].append(numb)

# print('')
# print('-=' * 30)
# print('[', *number_list[0][0], ']', '[', *number_list[0][1], ']', '[', *number_list[0][2], ']')
# print('[', *number_list[1][0], ']', '[', *number_list[1][1], ']', '[', *number_list[1][2], ']')
# print('[', *number_list[2][0], ']', '[', *number_list[2][1], ']', '[', *number_list[2][2], ']')
