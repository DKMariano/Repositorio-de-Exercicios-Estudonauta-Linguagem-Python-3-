# Desafio 063
# Escreva um programa que:
# - leia um número N inteiro qualquer
# - mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

print('')
print('-=-'*20)
print(f"{'SEQUÊNCIA DE FIBONACCI':^60}")
print('-=-'*20)
term = int(input('Quantos termos da sequência você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= term:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM!')
print('')
print('-=-'*20)
