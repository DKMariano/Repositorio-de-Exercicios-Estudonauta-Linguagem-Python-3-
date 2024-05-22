# Desafio 067
# Faça um programa que:
# - mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
# O programa será interrompido quando o número solicitado for negativo.

while True:
    print('-=-' * 10)
    multi = int(input('Quer ver a tabuada de qual valor?\n'))
    print(' ')
    print('-=-' * 10)
    print(f"{'TABUADA DE MULTIPLICAÇÃO': ^30}")
    print('-=-' * 10)
    if multi < 0:
        break
    for c in range(1, 11):
        print(f'{multi:2} x {c:2} = {c * multi:2}')
print('')
print('-=-'*10)
print(f'PROGRAMA DE TABUADA ENCERRADO! ')
print('Tenha um bom dia!')
