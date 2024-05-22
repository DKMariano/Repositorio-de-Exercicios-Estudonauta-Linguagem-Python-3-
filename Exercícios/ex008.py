# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

v = float(input('Digite o valor em metros: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
cm = v * 100
mm = v * 1000
print(' ')
print('-' * 40)
print('CONVERSOR DE MEDIDAS'.center(40))
print('_' * 40)
print(f'{v:.2f} m é igual a:')
print(f'- {km:.2f} km, ou ')
print(f'- {hm:.2f} hm, ou ')
print(f'- {dam:.2f} dam, ou ')
print(f'- {dm:.2f} dm, ou ')
print(f'- {cm:.2f} cm, ou ')
print(f'- {mm:.2f} mm, ou ')

# print('{} m em centímetros é igual a {} cm.'.format(v,c))
# print('{} m em milímetros é igual a {} mm'.format(v,m))
