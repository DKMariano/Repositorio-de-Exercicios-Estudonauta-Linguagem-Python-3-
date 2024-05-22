# Desafio 029
# Escreva um programa que leia a velocidade de um carro.
# Se o carro ultrapassar 80 km/h mostre ume mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 para cada km acima do limite

speed = int(input('Qual é a velocidade atual do seu carro? Km/h\n'))
traffic_ticket = (speed - 80) * 7
if speed > 80:
    print('VOCÊ FOI MULTADO!\nO limite de velocidade permitido é de 80 km/h')
    print(f'Você deve pagar uma multa de R$ {traffic_ticket:.2f}')
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('Parabéns!\nSua velocidade está dentro dos limites permitidos!')
    print('Tenha um bom dia! Dirija com segurança')
