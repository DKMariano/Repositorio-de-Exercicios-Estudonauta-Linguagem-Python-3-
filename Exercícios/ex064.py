# Desafio 64
# Crie um programa que:
# - leia vários números inteiros pelo teclado.
# - O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada.
# No final, mostre:
# - quantos números foram digitados
# - qual foi a soma entre eles (desconsiderando o flag).

n1 = s = cont = 0
while n1 != 999:
    n1 = int(input('Digite um número [Digite \"999\" se quiser parar]: '))
    if n1 != 999:
        cont += 1
        s += n1
print(f'Você digitou {cont} e a soma entre eles é {s}')
