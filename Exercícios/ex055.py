# Desafio 55
# Faça um programa que:
# - leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

fat = 0
thin = 0
for c in range(1, 6):
    weight = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        fat = weight
        thin = weight
    else:
        if weight > fat:
            fat = weight
        if weight < thin:
            thin = weight
print('')
print(f'O maior peso digitado foi de {fat} kg.')
print(f'O menor peso digitado foi de {thin} kg.')
print('')
