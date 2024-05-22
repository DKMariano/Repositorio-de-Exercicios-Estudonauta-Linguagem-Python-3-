# Desafio 073
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol
# Escreva os times na ordem de colocação.
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

camp_brasi = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
              'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia',
              'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('')
print('-=-' * 20)
print(f"{'BRASILEIRÃO SÉRIE A':^60}")
print('-=-' * 20)
print('')
print('Lista de times do Brasileirão: ')
pos = 0
for time in camp_brasi:
    pos += 1
    print(pos, '- ', time)
print('-' * 60)
print('Os 5 primeiros times são: ',)
five_team = camp_brasi[0:5]
pos = 0
for time in five_team:
    pos += 1
    print(pos, '- ', time)
print('-' * 60)
print('Os últimos 4 colocados são: ')
last_team = camp_brasi[-4:]
pos = 16
for time in last_team:
    pos += 1
    print(pos, '- ', time)
print('-' * 60)
print('Times em ordem alfabética: ')
order_team = sorted(camp_brasi)
for time in order_team:
    print(time)
print('-' * 60)
print(f'O time Fortaleza está na  {camp_brasi.index('Fortaleza')}ª posição.')
print('')
