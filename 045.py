from random import randint
from time import sleep
cores = {
'limpar':'\033[m',
'verde':'\033[32m',
'azul':'\033[34m',
'vermelho':'\033[31m',
'amarelo':'\033[33m',
'magenta':'\033[35m',
'ciano':'\033[36m'}

print('='*40)
titulo = print('          {}PEDRA PAPEL TESOURA{}'.format(cores['magenta'],cores['limpar']))
print('='*40)
confirmação = ''


while confirmação = 'Sim':

    jogador = int(input('''Escolha entre:
[0] Pedra
[1] Papel
[2] Tesoura
Escolha: '''))

    opções = [0,1,2]

    if jogador not in opções:
        jogador = 'erro'
        while jogador == 'erro':
            print('{}VALOR INVÁLIDO... ESCOLHA NOVAMENTE{}'.format(cores['vermelho'],cores['limpar']))
            sleep(2)
            jogador = int(input('''Escolha entre:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Escolha: '''))
            if jogador not in opções:
                jogador = 'erro'


    ppt = ['Pedra','Papel','Tesoura']

    print('Você escolheu {}{}{}'.format(cores['azul'],ppt[jogador],cores['limpar']))

    print('A máquina está escolhendo...')
    sleep(2)

    maquina = randint(0,2)
    print('A máquina escolheu {}{}{}'.format(cores['amarelo'],ppt[maquina],cores['limpar']))


    if maquina == jogador:
        print('{}EMPATE{}'.format(cores['azul'],cores['limpar']))

    elif jogador == 1 and maquina == 0 or jogador == 2 and maquina == 1 or jogador == 0 and maquina == 2:
        print('{}VITÓRIA{}'.format(cores['verde'],cores['limpar']))

    else:
        print('{}DERROTA{}'.format(cores['vermelho'],cores['limpar']))

    conferir = input('Deseja continuar? [SIM/NÃO]').upper().strip()
    if conferir == 'SIM':
        confirmação = 'Sim'
    else:
        quit()
    