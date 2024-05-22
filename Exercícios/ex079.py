# Desafio 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('')
numb_list = list()
while True:
    numb = int(input(f'Digite um número inteiro: '))
    if numb not in numb_list:
        numb_list.append(numb)
        print('Esse valor foi adicionado com sucesso.')
    else:
        print('Esse valor já foi digitado.')
    resp = input('Deseja digitar outro valor [S/N]? ').strip().upper()[0]
    if resp == "N":
        break
numb_list.sort()
print('-=-'*20)
print(f'Você digitou os valores {numb_list}')
