# Desafio 071
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro).
# O programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10, R$ 5.00 e R$1.

print('')
print('-=-' * 20)
print(f"{'BANCO NYMERIA':^60}")
print('-=-' * 20)
print('')
value = int(input('Qual valor que você deseja sacar? R$ '))
amount = value
cash = 50
money_bill = 0
while True:
    if amount >= cash:
        amount -= cash
        money_bill += 1
    else:
        if money_bill > 0:
            print(f'Total de {money_bill} cédulas de R$ {cash}.')
        if cash == 50:
            cash = 20
        elif cash == 20:
            cash = 10
        elif cash == 10:
            cash = 1
        money_bill = 0
        if amount == 0:
            break
print('')
print('-=-' * 20)
print('Obrigado por escolher a nossa empresa.')
print('É um prazer ter você como cliente.')
print('-=-' * 20)
print('')
