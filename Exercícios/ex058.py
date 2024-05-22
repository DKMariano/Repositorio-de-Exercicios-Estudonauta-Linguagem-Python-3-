# Desafio 058
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar
# Lembre-se de mostrar no final quantos palpites foram necessários para vencer.

from random import choice
from time import sleep
name = input("Qual é o seu nome?\n").strip().upper()
print('-=-'*20)
print(f'Olá, {name}! Vamos brincar?')
print('Eu pensei em um número entre 0 e 5. Tente advinhar!')
print('-=-'*20)
total = 0
player_number = int(input('Qual foi o número que pensei? \n'))
print('-=-'*20)
print('')
print('PROCESSANDO...')
sleep(3)
print('')
print('-=-'*20)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computer_number = choice(numbers)
while player_number != computer_number:
    total += 1
    if player_number > computer_number:
        print('-=-' * 20)
        print(f'Você errou! =/')
        print(f'O número que eu pensei é MENOR que {player_number}.')
        player_number = int(input('Tente de novo: \n'))
        print('-=-' * 20)
        print('')
        print('PROCESSANDO...')
        sleep(3)
        print('')
    elif player_number < computer_number:
        print('-=-' * 20)
        print(f'Você errou! =/')
        print(f'O número que eu pensei é MAIOR que {player_number}.')
        player_number = int(input('Tente de novo: \n'))
        print('-=-' * 20)
        print('')
        print('PROCESSANDO...')
        sleep(3)
        print('')
if total == 0:
    print('-=-' * 20)
    print('')
    print(f'Uau, {name}!')
    print(f'Você advinhou de primeira que eu pensei no número | {computer_number} |! o/')
    print('')
    print('-=-' * 20)
elif total == 1 or total == 2:
    print('-=-' * 20)
    print('')
    print(f'PARABÉNS, {name}!')
    print(f'Você precisou de apenas 1 tentativa para advinhar o número que pensei no número | {computer_number} |!')
    print('')
    print('-=-' * 20)
elif total == 3 or total == 4 or total == 5:
    print('-=-' * 20)
    print('')
    print(f'NADA MAL, {name}!')
    print(f'Após {total} tentativas, você advinhou que eu pensei no número | {computer_number} |!')
    print('')
    print('-=-' * 20)
elif total == 6 or total == 7 or total == 8:
    print('-=-' * 20)
    print('')
    print(f'Eita, {name}!')
    print(f'Você precisou de {total} tentativas para advinhar o número que eu pensei | {computer_number} |!')
    print('')
    print('-=-' * 20)
elif total == 9:
    print('-=-' * 20)
    print('')
    print(f'{name}, quase que você não acerta!')
    print(f'Você precisou de {total} tentativas para advinhar o número que eu pensei | {computer_number} |!')
    print('')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('')
    print(f'QUELERDEZA, {name}!')
    print(f'Você precisou de {total} tentativas, para advinhar que pensei no número | {computer_number} |!')
    print('')
    print('-=-' * 20)
