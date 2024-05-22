# Desafio 045
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

draw = (r'''
     _____ __  __ ____   _  _____ _____ _ 
    | ____|  \/  |  _ \ / \|_   _| ____| |
    |  _| | |\/| | |_) / _ \ | | |  _| | |
    | |___| |  | |  __/ ___ \| | | |___|_|
    |_____|_|  |_|_| /_/   \_\_| |_____(_)
    ''')
lost = (r'''
     _  ___   ____    _    ____   ___  ____  
    | |/ _ \ / ___|  / \  |  _ \ / _ \|  _ \ 
 _  | | | | | |  _  / _ \ | | | | | | | |_) |
| |_| | |_| | |_| |/ ___ \| |_| | |_| |  _ < 
 \___/ \___/ \____/_/__ \_\____/ \___/|_| \_\
|  _ \| ____|  _ \|  _ \| ____| | | | |      
| |_) |  _| | |_) | | | |  _| | | | | |      
|  __/| |___|  _ <| |_| | |___| |_| |_|      
|_|   |_____|_| \_\____/|_____|\___/(_)          
    ''')
win = (r'''
     _  ___   ____    _    ____   ___  ____  
    | |/ _ \ / ___|  / \  |  _ \ / _ \|  _ \ 
 _  | | | | | |  _  / _ \ | | | | | | | |_) |
| |_| | |_| | |_| |/ ___ \| |_| | |_| |  _ < 
_\___/ \___/_\____/_/ __\_\____/ \___/|_| \_\
\ \   / / ____| \ | |/ ___| ____| | | | |    
 \ \ / /|  _| |  \| | |   |  _| | | | | |    
  \ V / | |___| |\  | |___| |___| |_| |_|    
   \_/  |_____|_| \_|\____|_____|\___/(_)    
    ''')

print('')
print('-=-'*20)
print('JOKENPÔ'.center(60))
print('-=-'*20)
print('')
print('Suas opções:')
print("""[ 1 ] PEDRA
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
print("""[ 2 ] PAPEL
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
print("""[ 3 ] TESOURA
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
player = input('Qual é a sua jogada? ')
jokenpon = ["Pedra", "Papel", "Tesoura"]
pc = choice(jokenpon)
print('')
print('-'*60)
print('JO')
sleep(1)
print('')
print('KEN')
sleep(1)
print('')
print('PÔ')
sleep(1)
print('')
print('-'*60)
if player == "1":  # Jogador escolheu Pedra
    if pc == "Papel":
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Pedra.')
        print('-' * 60)
        print(lost)
    elif pc == "Tesoura":
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Pedra.')
        print('-' * 60)
        print(win)
    else:
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Pedra.')
        print('-' * 60)
        print(draw)
elif player == "2":  # Jogador escolheu Papel
    if pc == "Pedra":
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Papel.')
        print('-' * 60)
        print(win)
        print('_' * 60)
    elif pc == "Tesoura":
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Papel.')
        print('-' * 60)
        print(lost)
        print('_' * 60)
    else:
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Papel.')
        print('-' * 60)
        print(draw)
        print('_' * 60)
elif player == "3":  # Jogador escolheu Tesoura
    if pc == "Pedra":
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Tesoura.')
        print('-' * 60)
        print(lost)
        print('_' * 60)
    elif pc == "Papel":
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Tesoura.')
        print('-' * 60)
        print(win)
        print('_' * 60)
    else:
        print(f'O computador escolheu {pc}.')
        print(f'O jogador escolheu Tesoura.')
        print('-' * 60)
        print(draw)
        print('_' * 60)
else:
    print('\033[0:31m OPÇÃO DE PAGAMENTO INVÁLIDA!!\033[m')
    print('_' * 60)
