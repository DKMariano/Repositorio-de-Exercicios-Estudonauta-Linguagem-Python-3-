# Desafio 032
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import datetime
year = int(input('Qual ano você deseja analisar? (Digite 0 caso deseje analisar o ano atual)\n'))
if year == 0:
    year = datetime.now().year
else:
    year = year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano de {year} é BISSEXTO.')
else:
    print(f'O ano de {year} NÃO É BISSEXTO.')
