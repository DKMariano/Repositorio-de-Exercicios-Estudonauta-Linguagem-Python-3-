# Desafio 042: Refaça o DESAFIO 35 dos triângulos, acrescentando:
# - o recurso de mostrar que tipo de triângulo será formado:
# a) EQUILÁTERO: todos os lados iguais
# b) ISÓSCELES: dois lados iguais, um diferente
# c) ESCALENO: todos os lados diferentes

name = input('Qual é o seu nome?\n').upper()
print('')
print('-=-'*40)
print('ANALISADOR DE TRIÂNGULOS'.center(40))
print('-=-'*40)
print('')
print(f'Saudações, {name}!')
print('Esse é o ANALISADOR DE TRIÂNGULOS versão 2.0')
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
    if l1 == l2 == l3:
        print('O triângulo formado é do tipo \033[0:34mEQUILÁTERO.\033[m')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('O triângulo formado é do tipo  \033[0:34mESCALENO.\033[m')
    else:
        print('O triângulo formado é do tipo  \033[0:34mISÓCELES.\033[m')
else:
    print('As retas digitadas \033[0:31mNÃO\033[m podem formar um triângulo!')
print('')
print('-=-'*40)
print(f'{name}, obrigado por usar o ANALISADOR DE TRIÂNGULOS! ')
print('Tenha um bom dia!')
