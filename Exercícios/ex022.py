# Desafio 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar os espaços)
# - Quantas letras ao tem o primeiro nome
print(' ')
print('-'*90)
print(f"{'ANALISADOR DE NOMES':^80}")
print('_'*90)
print(' ')
nome_completo = input('Digite seu nome completo:\n')
nome_separado = nome_completo.split()
primeiro_nome = nome_separado[0]
print('Seu nome escrito apenas em letras maiúsculas é ', nome_completo.upper(), '.')
print('Seu nome escrito apenas em letras minúsculas é ', nome_completo.lower(), '.')
print('Seu nome tem ao todo ', len(nome_completo)-nome_completo.count(' '), ' letras.')
print('Seu primeiro nome é ', primeiro_nome, 'e tem ', len(primeiro_nome), 'letras.')
print('_'*90)
