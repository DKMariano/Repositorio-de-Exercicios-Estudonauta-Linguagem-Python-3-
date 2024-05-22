# Desafio 44: Elabore um programa que:
# - calcule o valor a ser pago por um produto.
# Considere que o seu preço normal e condição de pagamento são:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('')
print('-=-'*20)
print('LOJAS TABAJARA'.center(60))
print('-=-'*20)
print('')
price = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista (dinheiro/ pix)
[ 2 ] à vista no cartão
[ 3 ] 2 x no cartão
[ 4 ] 3 x ou mais no cartão
''')
choice = input('Qual é a opção desejada? ')
print('-' * 40)
if choice == "1":
    discount = price * 0.1
    pay = price - discount
    print(f'Valor do produto: R$ {price:.2f}')
    print(f'Valor do desconto: R$ {discount:.2f}')
    print(f'Total a pagar: R$ {pay:.2f}')
    print('_' * 40)
elif choice == "2":
    discount = price * 0.05
    pay = price - discount
    print(f'Valor do produto: R$ {price:.2f}')
    print(f'Valor do desconto: R$ {discount:.2f}')
    print(f'Total a pagar: R$ {pay:.2f}')
    print('_' * 40)
elif choice == "3":
    installment = 2
    pay = price / 2
    print(f'Valor do produto: R$ {price:.2f}')
    print(f'Forma de pagamento: {installment} parcelas de {pay:.2f}')
    print(f'Total a pagar: R$ {price:.2f}')
    print('_' * 40)
elif choice == "4":
    installment = float(input('Em quantas parcelas deseja dividir? '))
    fees = price * 0.2
    total_pay = (price + fees)
    pay = total_pay / installment
    print(f'Valor do produto: R$ {price:.2f}')
    print(f'Valor do juros: R$ {fees:.2f}')
    print(f'Forma de pagamento:{installment} parcelas de {pay:.2f}')
    print(f'Total a pagar: R$ {total_pay:.2f}')
    print('_' * 40)
else:
    print('\033[0:31m OPÇÃO DE PAGAMENTO INVÁLIDA!!\033[m')
    print('_' * 40)
