# Desafio 081
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

print('')
resp = ''
numb_list = list()
while resp != 'N':
    numb_list.append(int(input('Digite um número inteiro: ')))
    resp = input('Deseja continuar [S/N]? ').strip().upper()[0]
print('-=-' * 20)
len_numb_list = len(numb_list)
print(f'Você digitou {len_numb_list} números.')
numb_list.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numb_list}')
if 5 in numb_list:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 NÃO FAZ parte da lista!')
