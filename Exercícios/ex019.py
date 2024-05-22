# Desafio 019
# Um professor que sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que:
# - leia o nome dos alunos digitados
# - escolha um aluno
# - mostre o nome do aluno escolhido
from random import choice
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lis = [a1, a2, a3, a4]
s = choice(lis)
print(f'A pessoa escolhida para limpar o quadro é {s}. ')

# OU

# import random
# a1 = str(input('Digite o nome do primeiro aluno: '))
# a2 = str(input('Digite o nome do segundo aluno: '))
# a3 = str(input('Digite o nome do terceiro aluno: '))
# a4 = str(input('Digite o nome do quarto aluno: '))
# lis = (a1, a2, a3, a4)
# s = random.choice(lis)
# print(f'A pessoa escolhida para limpar o quadro é {s}. ')
