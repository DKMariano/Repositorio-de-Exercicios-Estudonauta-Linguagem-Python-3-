# Desafio 057
# Faça um programa que:
# - leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sex = input('Informe seu sexo:[M / F] ').strip().upper()[0]
while sex not in "FM":
    sex = input('Dado inválido. Por favor, informe o seu sexo: ').strip().upper()[0]
print(f'{sex} registrado com sucesso')
