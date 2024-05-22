# Desafio 56
# Desenvolva um programa que:
# - leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# - a média de idade do grupo
# - qual é o nome do homem mais velho
# - quantas mulheres têm menos de 20 anos.

ave_age = 0
total_age = 0
older_name = ''
older_age = 0
young_female = 0
for c in range(1, 5):
    print('-=-' * 20)
    print(f'{c:30}ª PESSOA')
    print('-=-' * 20)
    name = input('Nome: ').capitalize()
    age = int(input('Idade: '))
    sex: str = input('Sexo [M/F]: ')
    print('')
    total_age += age
    if c == 1 and sex in 'Mm':
        older_name = name
        older_age = age
    if sex in "Mm" and age > older_age:
        older_age = age
        older_name = name
    if sex in "Ff" and age < 20:
        young_female += 1
ave_age = total_age / 4
print('-=-' * 20)
print(f"{'ANÁLISE DO GRUPO':^60}")
print('-=-' * 20)
print('')
print(f'A média de idade do grupo é de {ave_age}.')
print(f'O home mais velho tem {older_age} e se chama {older_name}.')
print(f'Ao todo são {young_female} mulheres com menos de 20 anos.')
