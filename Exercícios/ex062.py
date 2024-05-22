# Desafio 062
# Melhore o DESAFIO 61, perguntando para o usuário se:
# - ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('')
print('-=-'*20)
print(f"{'PROGRESSÃO ARITMÉTICA':^60}")
print('-=-'*20)
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {total} termos mostrados!')
print('')
print('-=-'*20)
