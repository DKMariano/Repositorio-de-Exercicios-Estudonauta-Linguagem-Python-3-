# Desafio 082
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados.
# Ao final, mostre o conteúdo das três listas geradas.

print('')
numb_list = list()
odd_list = list()
even_list = list()
resp = ''

while resp != "N":
    numb_list.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar (S/N)? ').strip().upper()[0]

for numb in numb_list:
    if numb % 2 == 0:
        even_list.append(numb)
    else:
        odd_list.append(numb)

print('-=-' * 20)
print(f'A lista completa é {numb_list}')
print(f'A lista de pares é {even_list}')
print(f'A lista de ímpares é {odd_list}')
