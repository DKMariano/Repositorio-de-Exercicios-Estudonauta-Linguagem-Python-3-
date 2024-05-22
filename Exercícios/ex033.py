# Desafio 033
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o primeiro valor: '))
n3 = float(input('Digite o primeiro valor: '))
numbers = [n1, n2, n3]
max_value = max(numbers)
min_value = min(numbers)
print(f'O maior valor digitado foi {max_value:.2f}.')
print(f'O menor valor digitado foi {min_value:.2f}.')
