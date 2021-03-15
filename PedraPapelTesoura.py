'''
PEDRA, PAPEL e TESOURA
14/03/2021
'''
from random import choice
from time import sleep
ppt = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(ppt)
#inteface:
print('\033[1;33m','-=' * 25 +'\nPEDRA, PAPEL OU TESOURA:\n'+'-=' * 25,'\033[m')
escolha = input('Digite "Pedra", "Papel", ou "Tesoura":  ').upper()
sleep(1.0)
print('Eu escolho {}!'.format(computador))
sleep(2.0)
if escolha == computador:
    print('Ops! Nós dois escolhemos {}, vamos de novo.'.format(escolha))

elif escolha == 'PEDRA':
    if computador == 'PAPEL':
        print('\033[1;31mHA! Te ganhei, {} ganha de {}!\033[m'.format(computador, escolha))
    else:
        print('\033[1;32mVocê me ganhou! {} ganha de {}. :(\033[m'.format(escolha, computador))
elif escolha == 'PAPEL':
    if computador == 'TESOURA':
        print('\033[1;31mHA! Te ganhei, {} ganha de {}!\033[m'.format(computador, escolha))
    else:
        print('\033[1;32mVocê me ganhou! {} ganha de {}. :(\033[m'.format(escolha, computador))
elif escolha == 'TESOURA':
    if computador == 'PEDRA':
         print('\033[1;31mHA! Te ganhei, {} ganha de {}!\033[m'.format(computador, escolha))
    else:
        print('\033[1;32mVocê me ganhou! {} ganha de {}. :(\033[m'.format(escolha, computador))
else:
    print('\033[4;31mERRO! Tente de novo. Tenha certeza de digitar certo, o ANALFABETO!\033[m')
