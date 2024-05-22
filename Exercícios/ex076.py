# Desafio 076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('')
print('-=-' * 15)
print(f"{'LISTAGEM DE PREÇOS':^45}")
print('-=-' * 15)
tup = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor',
       '4.25', 'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')
for n in range(0, 16, 2):
    print(f'{tup[n].ljust(30, '.')}', 'R$', tup[n + 1].rjust(6))
print('-=-' * 15)
print('')

# for pos in range(0, len(tup)):
# if pos % 2 == 0:
# print(f'{tup[pos]:.<30}', end ='')
# else:
# print(f'{tup[pos]:>7}')
