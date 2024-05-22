# Desafio 015
# Escreva um programa que pergunte:
# - a quantidade de km pecorridos por um carro alugado
# - a quantidade de dias que o carro foi alugado
# Calcule o preço a pahar, sabendo que o carro custa R$ 60 por dia mais R$0.15 por km rodado

km = int(input('Quantos quilômetro (km) o carro percorreu? '))
d = float(input('Por quantos dias o carro ficou alugado? '))
a1 = (km * 0.15)
a2 = (d * 60)
t = a1 + a2

print(' ')
print('-' * 40)
print(f"{'CALCULADOR DE ALUGUEL'}")
print('_' * 40)
print(f'Total de dias: {d:.0f} dias')
print(f'Quilometragem: {km} km')
print(f'Valor da diária: R$ {a1:.2f}')
print(f'Valor da quilometragem: R${a2:.2f}')
print(f'Valor total do aluguel: R$ {t:.2f}')
