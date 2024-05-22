# Desafio 041:
# A Confederação Nacional de Natação precisa de um programa que:
# - leia o ano de nascimento de um atleta
# - mostre sua categoria, de acordo com a idade:
# a) Até 9 anos: MIRIM
# b) Até 14 anos: INFANTIL
# c) Até 19 anos: JÚNIOR
# d) Até 25 anos: SÊNIOR
# e) Acima de 25 anos: MASTER

from datetime import date
swimer = (r'''
                        .-"""-.
                       /       \
                      ;_.-"""-._;
   .,_       __,.---.-(=(o)-(o)=)-.---.,__       _,.
   '._'--"```          \   ^   /          ```"--'_.'
      ``"''~---~~%^%^.%.`._0_.'%,^%^%^~~---~''"``
   ~^~- `^-% ^~.%~%.^~-%-~.%-^.% ~`% ~-`%^`-~^~
         ~^- ~^- `~.^- %`~.%~-'%~^- %~^- ~^
''')
print(swimer)
print('')
print('-=-'*40)
print('Confederação Nacional de Natação'.center(40))
print('-=-'*40)
print('')
birth_year = int(input('Ano de Nascimento: '))
current_year = int(date.today().year)
age = current_year - birth_year
print(f'O atleta tem {age} anos.')
if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Classificação: INFANTIL')
elif age <= 19:
    print('Classificação: JÚNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
