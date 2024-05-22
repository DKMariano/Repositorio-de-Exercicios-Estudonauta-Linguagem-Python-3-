# Desafio 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente
# Ex: Ana Maria de Souza
# Primeiro: Ana, Último: Souza
name = input('Digite seu nome completo:\n').strip()
names_surname = name.split()
print('')
print('-'*80)
print('ANALISADOR DE NOME'.center(80))
print('_'*80)
print('')
print(f'Olá, {name}!\nMuito prazer em lhe conhecer!')
print(f'O seu prenome é {names_surname[0]}. ')
print(f'O seu último sobrenome é {names_surname[-1]}.')
print('_'*80)
