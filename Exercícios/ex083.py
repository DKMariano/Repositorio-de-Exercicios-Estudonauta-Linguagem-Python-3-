# Desafio 083
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


phrase_list = list(input('Digite uma expressão que use parênteses: \n'))
teste = list()
total = 0

for n in phrase_list:
    if n == '(' or n == ')':
        teste.append(n)

if int(len(teste)) % 2 != 0:
    print('Sua expressão está errada!')
else:
    if teste[0] != '(':
        print('Sua expressão está errada!')
    else:
        for u in range(len(teste), 2):
            if teste[u] != '(' and teste[u+1] != ')':
                print('Sua expressão está errada!')
                break
        print('Sua expressão está correta!')

# expr = str(input('Digite a expressão: '))
# pilha = [ ]
# for simb in expr:
    # if simb == '(':
        # pilha.append('(')
    # elif simb == ')':
        # if len(pilha) > 0
            # pilha.pop()
        # else:
            # pilha.append(')')
            # break
# if len(pilha == 0):
    # print('Sua expressão está válida!')
# else:
    # print('Sua expressão está errada!')
