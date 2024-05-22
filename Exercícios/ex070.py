# Desafio 070
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# - qual é o total gasto na compra.
# - quantos produtos custam mais de R$1000.
# - qual é o nome do produto mais barato.

from time import sleep
print('')
print('-=-' * 20)
print(f"{'LOJA SUPER TEKA':^60}")
print('-=-' * 20)
cheap_product = ''
total_product = total_price = expensive_product = cheap_price = 0
while True:
    print('')
    product = input('Nome do produto: ').upper()
    price = float(input('Preço: R$ '))
    total_price += price
    total_product += 1
    if price > 1000:
        expensive_product += 1
    if total_product == 1 or price < cheap_price:
        cheap_price = price
        cheap_product = product
    stop_flag = input('Quer continuar [S/N]? ').strip().upper()[0]
    while stop_flag not in 'SN':
        stop_flag = input('Quer continuar [S/N]? ').strip().upper()[0]
    if stop_flag == 'N':
        break
print('')
print('-=-' * 20)
print('Analisando as compras...')
sleep(1)
print('Por favor, aguarde um momento!')
sleep(1)
print('-=-' * 20)
print('')
print(f'Total da compra: R$ {total_price:.2f}.')
print(f'Total de produtos custando mais de R$1000.00: {expensive_product}.')
print(f'Produto mais barato:  {cheap_product} que custa R$ {cheap_price:.2f}.')
print('')
print('Obrigado por confiar na nossa loja!')
print('Por favor, volte sempre! =)')
print('-=-' * 20)
