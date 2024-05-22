# Desafio 084
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.


group = list()
date = list()
fat = thin = 0

while True:
    date.append(input('Nome: '))
    date.append(float(input('Peso: ')))
    if len(group) == 0:
        fat = thin = date[1]
    else:
        if date[1] >= fat:
            fat = date[1]
        if date[1] <= thin:
            thin = date[1]
    group.append(date[:])
    date.clear()
    resp = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if resp == 'N':
        break

print(f'Ao todo, você cadastrou {len(group)} pessoas')
print(f'O MAIOR peso cadastrado foi {fat:.2f}. As pessoas mais pesadas são: ', end='')
for person in group:
    if person[1] == fat:
        print(person[0], end='... ')
print(f'\nO MENOR peso cadastrado foi {thin:.2f}. As pessoas menos pesadas são: ', end='')
for person in group:
    if person[1] == thin:
        print(person[0], end='... ')
