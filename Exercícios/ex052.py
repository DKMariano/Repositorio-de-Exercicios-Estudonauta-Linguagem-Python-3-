# Desafio 052: Faça um programa que:
# - leia um número inteiro
# - diga se ele é ou não um número primo.


n = int(input('Digite um número inteiro: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(' ')
print(f'\033[mO número {n} é divisível por {t} números.')
if t > 2:
    print(f'Por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele É PRIMO!')
