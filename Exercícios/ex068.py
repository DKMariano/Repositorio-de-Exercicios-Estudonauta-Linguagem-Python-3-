# Desafio 068
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder.
# No final do jogo, mostre o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
# Imagens de jogo em ASCII Art
lose = (r'''
 __      __        //\                      _            _ 
 \ \    / /       |/ \|                    | |          | |
  \ \  / /__   ___ ___   _ __   ___ _ __ __| | ___ _   _| |
   \ \/ / _ \ / __/ _ \ | '_ \ / _ \ '__/ _` |/ _ \ | | | |
    \  / (_) | (_|  __/ | |_) |  __/ | | (_| |  __/ |_| |_|
     \/ \___/ \___\___| | .__/ \___|_|  \__,_|\___|\__,_(_)
                        | |                                
                        |_|                                
    ''')
win = (r'''
  __      __        //\                     _                 _ 
 \ \    / /       |/ \|                   | |               | |
  \ \  / /__   ___ ___    __ _  __ _ _ __ | |__   ___  _   _| |
   \ \/ / _ \ / __/ _ \  / _` |/ _` | '_ \| '_ \ / _ \| | | | |
    \  / (_) | (_|  __/ | (_| | (_| | | | | | | | (_) | |_| |_|
     \/ \___/ \___\___|  \__, |\__,_|_| |_|_| |_|\___/ \__,_(_)
                          __/ |                                
                         |___/                                 
       ''')
game_over = (r'''
      _____          __  __ ______    ______      ________ _____  
     / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
    | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
    | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
    | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
     \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\

    ''')

print('')
print('-=-'*10)
print(f"{'PAR OU ÍMPAR':^30}")
print('-=-'*10)
print('')
victory = 0
while True:
    num = int(input('Digite um valor inteiro: '))
    user_choice = ' '
    while user_choice not in "PI":
        user_choice = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    pc_choice = random.randrange(0, 10)
    total = num + pc_choice
    result = total % 2
    print('')
    print('-=-' * 10)
    print(f'Você jogou {num} e o computador {pc_choice}.')
    if result == 0:
        if user_choice == 'P':
            victory += 1
            print(f'O total deu {total} que é PAR.')
            print(win)
            print('-=-' * 10)
            print('')
        else:
            print(f'O total deu {total} que é PAR.')
            print(lose)
            print('-=-' * 10)
            print('')
            break
    else:
        if user_choice == 'I':
            victory += 1
            print(f'O total deu {total} que é ÍMPAR.')
            print(win)
            print('-=-' * 10)
            print('')
        else:
            print(f'O total deu {total} que é ÍMPAR.')
            print(lose)
            print('-=-' * 10)
            print('')
            break
if victory == 0:
    print('Que pena! Você não conseguiu vencer nem uma vez!')
elif victory > 1:
    print(f'Você venceu {victory} vezes.')
else:
    print(f'Você venceu {victory} vez.')
print('')
print('-=-' * 10)
print(game_over)
print('')
print('-=-'*10)
