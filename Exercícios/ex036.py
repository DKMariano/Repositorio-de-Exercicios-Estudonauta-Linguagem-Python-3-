# Desafio 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

home = float(input('Qual o valor da casa que você quer comprar?\n'))
salary = float(input('Qual é o valor do seu salário?\n'))
years = int(input('Por quantos anos você vai financiar a casa?\n'))
financing = home / (years * 12)
installment = 0.3 * salary
print(f'Para pagar uma casa de R$ {home:.2f} a prestação será de R$ {financing:.2f}')
if financing >= installment:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
