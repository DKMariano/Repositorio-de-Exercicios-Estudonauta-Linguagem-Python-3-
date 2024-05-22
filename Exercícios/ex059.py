# Desafio 059
# Crie um programa que:
# - leia dois valores
# - mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


a = 0
m = 0
big = 0
option = ' '
n1 = float(input(' Digite o primeiro valor: '))
n2 = float(input(' Digite o segundo valor: '))

while option != "5":
    print('-=-' * 10)
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa    
        ''')
    print('-=-' * 10)
    option = input('>>>>> Qual é sua opção? ')
    if "1" < option > "5":
        print('\033[31mOpção inválida! Tente novamente. \033[m')
    elif option == "1":
        a = n1 + n2
        print(f'A soma entre {n1} e {n2} é {a}.')
    elif option == "2":
        m = n1 * n2
        print(f'A multiplicando {n1} com {n2} o resultado é {m}.')
    elif option == "3":
        a = [n1, n2]
        m = max(a)
        print(f'O maior número digitado é {m}.')
    elif option == "4":
        print('Digite os novos valores:')
        n1 = float(input(' Digite o primeiro valor: '))
        n2 = float(input(' Digite o segundo valor: '))
print('Obrigado por usar nosso programa!')
print('Tenha um bom dia!')
