# Desafio 072
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezonove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Número Inválido. Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {ext[num]}')
        resp = input('Quer continuar [S / N]? ').upper().strip()[0]
        while resp not in 'SN':
            resp = input('Quer continuar [S / N]? ').upper().strip()[0]
        if resp == 'N':
            break
