# Desafio 069
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# - quantas pessoas tem mais de 18 anos.
# - quantos homens foram cadastrados.
# - quantas mulheres tem menos de 20 anos.

legal_age = total_male = young_female = 0
resp = ''
while True:
    print('')
    print('-=-' * 20)
    print(f"{'CADASTRO DE PESSOAS':^60}")
    print('-=-' * 20)
    age = int(input('Idade: '))
    sex = input('Sexo [M/F]: ').strip().upper()[0]
    while sex not in 'MF':
        sex = input('Sexo [M/F]: ').strip().upper()[0]
    if age >= 18:
        legal_age += 1
    if sex == 'M':
        total_male += 1
    elif sex == 'F' and age < 20:
        young_female += 1
    resp = input('Quer Continuar [S/N]? ').strip().upper()[0]
    while resp not in 'NS':
        resp = input('Quer Continuar [S/N]? ').strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {legal_age}.')
print(f'Total de homens: {total_male}.')
print(f'Total de mulheres com menos de 20 anos: {young_female}.')
