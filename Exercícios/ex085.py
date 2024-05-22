# Desafio 085
# Crie um programa que:
# - o usuário possa digitar sete valores numéricos
# - cadastre os números digitados em uma lista única
# - mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.


list_number = [[], []]

for number in range(1, 8):
    numb = int(input(f'Digite o {number}o. valor: '))
    if numb % 2 == 0:
        list_number[0].append(numb)
    else:
        list_number[1].append(numb)

list_number[0].sort()
list_number[1].sort()

print(f'Os valores PARES digitados foram: {list_number[0]}')
print(f'Os valores ÍMPARES digitados foram: {list_number[1]}')
