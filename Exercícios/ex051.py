# Desafio 051: Desenvolva um programa que:
# - leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('')
print('-=-'*20)
print(f"{'PROGRESSÃO ARITMÉTICA':^60}")
print('-=-'*20)
n = int(input('Digite o primeiro termo: '))
pa = int(input('Digite a razão: '))
f = n + (10-1) * pa
for c in range(n, f + pa, pa):
    print(c, end=' -> ')
print('Acabou!')
print('')
print('-=-'*20)