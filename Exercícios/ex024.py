# Desafio 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
citty = input("Em que cidade que você nasceu? ")
cidade = citty.lower()
resposta = 'santo' in cidade
print(resposta)
