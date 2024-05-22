# Desafio Python 077
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tup = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
       'PROGRAMADOR', 'FUTURO')
for word in tup:
    print(f'\nNa palavra {word} temos ', end='')
    for vowel in word:
        if vowel.upper() in 'AEIOU':
            print(vowel, end=' ')
