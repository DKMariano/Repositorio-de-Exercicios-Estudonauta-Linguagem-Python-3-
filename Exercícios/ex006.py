# Desafio 006
# Faça um algoritmo que leia um número e mostre o seu dobro, seu triplo e a raiz quadrada.

n = int(input('Digite um número inteiro: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} é igual a {d}')
print(f'O triplo de {n} é igual a {t}')
print(f'A raiz quadrada de {n} é igual {r:.2f}.')

# print('O dobro de {} é igual a {}'.format(n, d))
# print('O triplo de {} é igual a {}'.format(n, t))
# print('A raiz quadrada de {} é igual {:.2}'.format(n, r))
# pow(n,(1/2))
