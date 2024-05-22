# Desafio 020
# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a1 = str(input('Primeiro estudante: '))
a2 = str(input('Segundo estudante: '))
a3 = str(input('Terceiro estudante: '))
a4 = str(input('Quarto estudante: '))
lis = [a1, a2, a3, a4]
shuffle(lis)
print(f'A ordem para aparesentação dos trabalhos é: {lis} ')

# import random
# a1 = str(input('Primeiro estudante: '))
# a2 = str(input('Segundo estudante: '))
# a3 = str(input('Terceiro estudante: '))
# a4 = str(input('Quarto estudante: '))
# lis = [a1, a2, a3, a4]
# random.shuffle(lis)
# print(f'A ordem para apresentação dos trabalhos é: {l}.')
