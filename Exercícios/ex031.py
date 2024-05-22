# Desafio 031
# Desenvolva um programa que:
# - pergunte a distância de uma viagem em km
# - calcule e mostre na tela o preço da passagem
# O preço da passagem é R$ 0,50 por km para viagens de até 200 km
# O preço da passagem é R$ 0,45 para viagens mais longas

distance = float(input('Qual é a distância total da sua viagem?(Km)\n'))
price = distance * 0.5 if distance <= 200 else distance * 0.45
print(f'O preço da passagem de uma viagem de {distance:.2f} km é R$ {price:.2f}.')

# distance = float(input('Qual é a distância total da sua viagem?(Km)\n'))
# price = distance * 0.5
# price_promo = distance * 0.45
# if distance > 200:
# print(f'O preço da passagem de uma viagem de {distance:.2f} km é R$ {price_promo:.2f}.')
# else:
# print(f'O preço da passagem de uma viagem de {distance:.2f} km é R$ {price:.2f}.')
