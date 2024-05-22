# Desafio 061
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA
# mostre os 10 primeiros termos da progressão usando a estrutura while.

print('')
print('-=-'*20)
print(f"{'PROGRESSÃO ARITMÉTICA':^60}")
print('-=-'*20)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM!')
print('')
print('-=-'*20)

# n = int(input('Digite o primeiro termo: '))
# common_difference = int(input('Digite a razão: '))
# last_term = n + (10-1) * pa
# first_term = n
# print(f'{first_term} -> ', end='')
# while first_term  != last_term:
#       first_term  += common_difference
#       print(first_term, end=' -> ')
