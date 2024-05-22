# Desafio 080: Crie um programa no qual o usuário cadastre cinco valores numéricos digitados em uma lista.
# Os números devem ser cadastrados já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

numb_list = list()
for position in range(0, 5):
    numb = int(input('Digite um número inteiro: '))
    if position == 0 or numb > numb_list[-1]:
        numb_list.append(numb)
        print(f'O número {numb} foi adicionado no final da lista.')
    else:
        count = 0
        while count < len(numb_list):
            if numb < len(numb_list):
                numb_list.insert(1, numb)
                print(f'O número {numb} foi adicionado na posição {count} da lista.')
                break
            count += 1
print('-=- * 30')
print(f'Os valores digitados em ordem foram {numb_list}')
