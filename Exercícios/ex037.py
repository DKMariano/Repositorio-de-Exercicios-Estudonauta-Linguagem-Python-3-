# Desafio 037:
# Escreva um programa em Python que:
# - leia um número inteiro qualquer
# - peça para o usuário escolher qual será a base de conversão:
# - 1 para binário,
# - 2 para octal
# - a3 para hexadecimal.

num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
base = input('Sua opção: ')
if base == '1':
    bin_num = bin(num)
    print(f'{num} convertido para BINÁRIO é igual a {bin_num[2:]}.')
elif base == '2':
    oct_num = oct(num)
    print(f'{num} convertido para OCTAL é igual a {oct_num[2:]}.')
elif base == '3':
    hexa_num = hex(num)
    print(f'{num} convertido para HEXADECIMAL é igual a {hexa_num[2:]}.')
else:
    print('Erro: ESCOLHA INVÁLIDA')
