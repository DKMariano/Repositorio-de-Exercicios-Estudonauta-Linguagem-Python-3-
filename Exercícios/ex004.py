# Desafio 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis:

n = input('Digite algo:  ')
print('O tipo primitivo do que foi digitado é  ', type(n))
print('É um número?  ', n.isnumeric())
print('É um decimal?  ', n.isdecimal())
print('É um digito?  ', n.isdigit())
print('É uma letra do alfabeto?  ', n.isalpha())
print('Possui letras maiúsculas?  ', n.isupper())
print('Possui letras minúsculas?  ', n.islower())
print('Está capitalizada?  ', n.istitle())
print('É alfanumérico?  ', n.isalnum())
print('É um caractere do ASCII?  ', n.isascii())
print('É um espaço?  ', n.isspace())
print('É imprimível?  ', n.isprintable())
print('Pertence a uma subclasse?  ', n.__init_subclass__())
print('É um identificador? ', n.isidentifier())
