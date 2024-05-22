# Desafio 054:
# Crie um programa que:
# - leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime
old = 0
young = 0
current_year = datetime.now().year
for c in range(1, 8):
    birth_year = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    age = current_year - birth_year
    if age >= 18:
        old += 1
    else:
        young += 1
print('')
print(f'Ao todo tivemos {old} pessoas maiores de idade.')
print(f'Ao todo tivemos {young} pessoas maiores de idade.')
