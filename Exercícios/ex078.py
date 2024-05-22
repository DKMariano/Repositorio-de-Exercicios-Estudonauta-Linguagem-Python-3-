# Desafio 078
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print('')
numb_list = list()
for c in range(0, 5):
    numb_list.append(int(input(f'Digite um número para a posição {c}: ')))
print('')
print('-=-'*20)
print('')
print(f'Os valores digitados foram: {numb_list}')
print(f'O maior valor digitado foi {max(numb_list)} nas posições: ', end='')
for p, n in enumerate(numb_list):
    if n == max(numb_list):
        print(p, end='... ')
print(f'\nO menor valor digitado foi {min(numb_list)} nas posições: ', end='')
for q, n in enumerate(numb_list):
    if n == min(numb_list):
        print(q, end='... ')

# listanum = []]
# mai = 0
# men = 0
# for c in range(0, 5):
# # numb_list.append(int(input(f'Digite um número para a posição {c}: ')))
# # if c == 0:
    # mai = men = listanum[c]
    # else:
    # if listanum[c] > mai:
        # mai = listanum[c]
    # if listanum[c] < men:
        # men = listanum[c]
# print('-=-'*30)
# print(f'Você digitou os valores  {numb_list}')
# print(f'O maior valor digitado foi {mai} nas posições ', end='')
# for i, v in enumerate(listanum):
    # if v == mai:
        # print(f'{i}...', end='')
# print()
# print(f'O menor valor digitado foi {men} nas posições: ', end='')
# for i, v in enumerate(listanum):
    # if v == men):
        # print(f'{i}...', end='')
