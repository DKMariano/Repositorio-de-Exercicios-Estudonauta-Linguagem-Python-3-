# Desafio 028
# Escreva um programa que:
# - faça o computador "pensar" em um número inteiro entre 0 e 5
# - e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import choice
from time import sleep
name = input("Qual é o seu nome?\n").upper()
print('-=-'*20)
print(f'Olá, {name}! Tudo bom?')
print('Eu pensei em um número entre 0 e 5. Tente advinhar!')
print('-=-'*20)
player = int(input('Qual foi o número que pensei? '))
print('PROCESSANDO...')
sleep(3)
numbers = [0, 1, 2, 3, 4, 5]
computer = choice(numbers)
if player == computer:
    print(f'PARABÉNS, {name}! Você advinhou que eu pensei no número | {computer} |! o/')
else:
    print(f'Eu GANHEI! XD \nEu pensei no número | {computer} | e não no | {player} |!')
