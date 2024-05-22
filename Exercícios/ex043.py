# Desafio 043
# Desenvolva uma lógica que
# - leia o peso e a altura de uma pessoa
# - calcule seu Índice de Massa Corporal (IMC)
# mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
scale = (r'''
             _____              ________
,--'  |  `--.      .--'578.3 kg`--.
|mb`-._,-'fh|      |mb`-.____,-'fh|
|           |      |              |
|           |      |              |
|           |      |              |
|           |      |              |
|           |      |              |
`._________,'      `.____________.'
''')
name = input('Qual é o seu nome?\n').upper()
print('')
print('-=-'*40)
print('CALCULADORA DE IMC'.center(40))
print('-=-'*40)
print('')
print(f'Saudações, {name}!')
print('Esse é a CALCULADORA DE IMC versão 2.0')
print('Responda as perguntas abaixo para calcular o seu IMC')
print('-=-'*40)
print('PERGUNTAS')
height = float(input('Qual é a sua altura em metros?(Ex: 1.55):\n'))
weight = float(input('Qual é o seu peso em kg (Ex: 72):\n'))
bmi = weight / pow(height, 2)
print('-=-'*40)
print('')
print(f'{name}, o seu IMC é de {bmi:.1f}')
if bmi < 18.5:
    print(f"\033[0:31mVocê está ABAIXO da faixa do PESO IDEAL!\033[m")
elif 18.5 <= bmi < 25:
    print(f"Parabéns,\033[0:32m {name}!Você está na faixa do PESO IDEAL!\033[m")
elif 25 <= bmi < 30:
    print('\033[0:31mVocê está com SOBREPESO!\033[m')
elif 30 <= bmi < 40:
    print(f'\033[0:31m Cuidado, {name}! Você está com OBESIDADE!\033[m')
else:
    print('\033[0:31m Cuidado, {name}! Você está com OBESIDADE MÓRBIDA!\033[m')
print('')
print('-=-'*40)
print(f'{name}, obrigado por usar a CALCULADORA DE IMC!\033[m')
print('Tenha um bom dia!')
