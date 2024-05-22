# Desafio 049
# Refaça o DESAFIO 009, mostrando:
#  - a tabuada de um número que o usuário escolher
#  - só que agora utilizando um laço for.

n = int(input('Digite um número inteiro para ver sua tabuada: '))
print(' ')
print('-=-' * 10)
print(f"{'TABUADA DE MULTIPLICAÇÃO': ^30}")
print('-=-' * 10)
print(' ')
for c in range(0, 11):
    print(f'{n} x {c:2} = {n * c}')
