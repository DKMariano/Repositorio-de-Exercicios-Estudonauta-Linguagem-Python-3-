# Desafio 010
# Crie um programa  que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input('Quantos reais você tem na sua carteira? R$ '))
d = r / 4.922
e = r / 5.333
lb = r / 6.255
y = r / 0.033
print(' ')
print('-' * 40)
print('CONVERSOR DE MOEDAS'.center(40))
print('_' * 40)
print(f'R$ {r} = US$ {d:.2f}')
print(f'R$ {r} =   € {e:.2f}')
print(f'R$ {r} =   £ {lb:.2f}')
print(f'R$ {r} =   ¥ {y:.2f}')
