# Desafio 038:
# Escreva um programa que:
# - leia dois números inteiros e compare-os
# - Mostre na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    print(f'O maior número é {n1} e o menor é {n2}.')
elif n2 > n1:
    print(f'O maior número é {n2} e o menor é {n1}.')
else:
    print(f'Não existe um número maior, pois os dois são iguais.')
