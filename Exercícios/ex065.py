# Desafio 065
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre:
# - a média entre todos os valores
# - qual foi o maior
# - o menor valor lidos
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numb = add = count = lit = ave = big = 0
resp = ' '
while resp != 'N':
    numb = int(input('Digite um número: '))
    add += numb
    count += 1
    if count == 1:
        big = lit = numb
    else:
        if numb > big:
            big = numb
        elif numb < lit:
            lit = numb
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
ave = add / count
print(f'Você digitou {count} números e a média foi de {ave}.')
print(f'O maior valor foi {big} e o menor foi de {lit}.')
