# Desafio 053: Crie um programa que:
# - leia uma frase qualquer
# - diga se ela é um palíndromo, desconsiderando os espaços.

phrase = input('Digite uma frase:\n').upper()
phrase_space = phrase.replace(' ', '')
phrase_invert = phrase_space[::-1]
print(f'O inverso de {phrase_space} é {phrase_invert}')
if phrase_invert == phrase_space:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
