from random import randint
from time import sleep
item= ('pedra','papel','tesoura')
computador= randint(0,2)
print('''suas opções
[0] pedra
[1] papel
[2] tesoura''')
jogador= int(input('qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!')
print('-='*11)
print('o computador jogou {}'.format(item[computador]))
print('o jogador escolheu {}'.format(item[jogador]))
print('-='*11)
if computador==0:
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('jogadoor vence')

    elif jogador== 2:
        print('computador vence')

    else:
        print('jogada invalida')
elif computador== 1:
    if jogador==0:
        print('computador vence')
    elif jogador== 1:
        print('jogador empate')
    elif jogador== 2:
        print('jogador vence')
    else:
        print('empate')
elif computador== 2:
    if jogador==0:
        print('jogador vence')

    elif jogador== 1:
        print('computador vence')
    elif jogador== 2:
        print('empate')
