# Desafio 048
# Faça um programa que:
# - calcule a soma entre todos os números ímpares que
# a) são múltiplos de três se encontram no intervalo de 1 até 500.
t = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        t += 1
        s += c
print('')
print(f'A soma de todos os {t} valores solicitados é {s}.')
