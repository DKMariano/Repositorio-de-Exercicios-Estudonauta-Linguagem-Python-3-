# Desafio 075
# Desenvolva um programa que:
# - leia quatro valores pelo teclado
# - guarde-os em uma tupla.
# No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

tup = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {tup}.')
print(f'O valor 9 apareceu {tup.count(9)} vezes.')
if 3 in tup:
    print(f'O valor 3 apareceu na {tup.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 foi digitado em nenhuma posição.')
print(f'Números pares digitados forem ', end='')
for n in tup:
    if n % 2 == 0:
        print(n, end=' ')
