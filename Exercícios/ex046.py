# Desafio 046
# Faça um programa que:
# - mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print(r'''
      .' |
    .'   |
    /`-._'
   /   /
  /   /
 /   /
(`-./
 )
''')
print('Vamos começar a contagem regressiva para os fogos de artifício!')
print('')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('')
print(r'''
       .''.      .        *''*    :_\/_:     .
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::.  | ' *''*    * '.\'/.'_\(/_'.':'.'
 : /\ : :::::  =  *_\/_*     -= o =- /)\    '  *
  '..'  ':::' === * /\ *     .'/.\'.  ' ._____
      *        |   *..*         :       |.   |' .---"|
        *      |     _           .--'|  ||   | _|    |
        *      |  .-'|       __  |   |  |    ||      |
     .-----.   |  |' |  ||  |  | |   |  |    ||      |
 ___'       ' /"\ |  '-."".    '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
