# Desafio 039:
# Faça um programa que:
# - leia o ano de nascimento de um jovem
# - informe se ele ainda vai se alistar ao serviço militar
# - se é a hora exata de se alistar
# - ou se já passou do tempo do alistamento.
# - Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
birth_year = int(input('Ano de nascimento: '))
current_year = int(date.today().year)
age = int(current_year - birth_year)
print(f'Quem nasceu em {birth_year} tem {age} anos de idade em {current_year}.')
if age < 18:
    age_enlistment = 18 - age
    year_enlistment = birth_year + 18
    print(f'Ainda faltam {age_enlistment} anos para o alistamento.')
    print(f'Seu alistamento será em {year_enlistment}.')
elif age > 18:
    age_enlistment = age - 18
    year_enlistment = birth_year + 18
    print(f'Você já deveria ter se alistado há {age_enlistment} anos.')
    print(f'Seu alistamento foi no ano de {year_enlistment}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!!')
