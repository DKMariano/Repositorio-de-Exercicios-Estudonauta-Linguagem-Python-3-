# Desafio 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
a = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1+n2) / 2
print(' ')
print('-'*40)
print('CALCULADORA DE NOTAS'.center(40))
print('_'*40)
print(f'Aluno: {a}')
print(f'Nota da primeira avaliação: {n1}')
print(f'Nota da segunda avaliação: {n2}')
print('Média: {}'.format(m))
print('_'*40)

# print('Aluno: {}'.format(a))
# print('Nota da primeira avaliação: {}'.format(n1))
# print('Nota da segunda avaliação: {}'.format(n2))
