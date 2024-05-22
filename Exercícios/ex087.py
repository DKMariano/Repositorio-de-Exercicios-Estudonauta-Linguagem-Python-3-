# Desafio 087
# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even_numb = 0

for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))


print('=-' * 30)

for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}]', end='')
        if matrix[line][column] % 2 == 0:
            even_numb += matrix[line][column]
    print('')

print('=-' * 30)
print(f'A soma dos valores pares é {even_numb}.')

third_column = matrix[0][2] + matrix[1][2] + matrix[2][2]
print(f'A soma dos valores da terceira coluna é {third_column}.')

second_line = max(matrix[1])
print(f'O maior valor da sehunda linha é {second_line}.')
