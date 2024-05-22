# Desafio 035
# Desenvolva um programa que:
# - leia o comprimento de três retas
# - diga ao usuário se elas podem ou não formar um triângulo.

name = input('Qual é o seu nome?\n').upper()
print('')
print('-=-'*40)
print('ANALISADOR DE TRIÂNGULOS'.center(40))
print('-=-'*40)
print('')
print(f'Saudações, {name}!')
print('Esse é o ANALISADOR DE TRIÂNGULOS versão 1.0')
print('Responda as perguntas abaixo para saber se as condições de existência do triangulo estão presentes!')
print('-=-'*40)
print('PERGUNTAS')
l1 = float(input('Informe o tamanho da primeira reta: '))
l2 = float(input('Informe o tamanho da primeira reta: '))
l3 = float(input('Informe o tamanho da primeira reta: '))
print('-=-'*40)
print('')
if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print('As retas digitadas \033[0:32mPODEM\033[m formar um triângulo!')
else:
    print('As retas digitadas \033[0:31mNÃO\033[m podem formar um triângulo!')
print('')
print('-=-'*40)
print(f'{name}, obrigado por usar o ANALISADOR DE TRIÂNGULOS! ')
print('Tenha um bom dia!')
