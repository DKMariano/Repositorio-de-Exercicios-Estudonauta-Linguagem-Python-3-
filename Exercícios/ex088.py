# Desafio 088
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60, para cada jogo.
# Depois, cadastre tudo em uma lista composta.

from random import randint

print('')
print('-=' * 30)
print(f"{'GERADOR DE JOGOS DA MEGA SENA':^60}")
print('-=' * 30)
print('')

games_list = list()
temporary_list = list()
numb_games = int(input('Quantos jogos você quer que eu sorteie? '))

print()
print('-' * 60)
print(f"{'JOGOS':^60}")
print('-' * 60)

for number in range(0, numb_games):
    count = 0
    while True:
        num = randint(1, 60)
        if num not in temporary_list:
            temporary_list.append(num)
            count += 1
        if count >= 6:
            break
    temporary_list.sort()
    games_list.append(temporary_list[:])
    temporary_list.clear()

for number in range(len(games_list)):
    print(f'Jogo {number + 1}: {games_list[number]}')

print('')
print('-' * 60)
print('Obrigado por usar  o GERADOR DE JOGOS DA MEGA SENA.')
print('Desejamos SORTE nos seus jogos!!')
print('-' * 60)
print('')
