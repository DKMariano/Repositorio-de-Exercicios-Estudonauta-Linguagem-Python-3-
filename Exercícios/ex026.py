# Desafio 026
# Faça um programa que leia uma frase digitada e mostre
# - Quantas vezes aparece a letra "A"
# - Em que posição a letra "A" aparece pela primeira vez
# - Em que posição a letra "A" aparece pela ultima vez

phrase = input('Digite uma frase: ').lower().strip()
print(f'A letra A aparece {phrase.count('a')} vezes na frase.')
print(f'A letra A aparece pela primeira vez na posição {phrase.find('a') + 1}')
print(f'A letra A aparece pela última vez na posição {phrase.rfind('a') + 1}')
