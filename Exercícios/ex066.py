# Desafio 66
# Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre:
# - quantos números foram digitados
# - qual foi a soma entre elas (desconsiderando o flag).

counter = addition = 0
while True:
    n = int(input('Digite um valor [Digite 999 para parar]: '))
    if n == 999:
        break
    else:
        counter += 1
        addition += n
print(f'A soma dos {counter} valores foi {addition}.')
