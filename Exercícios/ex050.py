# Desafio 050:
# Desenvolva um programa que:
# - leia seis números inteiros
# - mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.
t = 0
s = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        t += 1
        s += n
print(f'Você digitou {t} número(s) par(es) e a soma deles é igual a {s}')
