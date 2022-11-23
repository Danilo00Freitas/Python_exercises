import random
from time import sleep

cores = {
'verde':'\033[32m',
'vermelho':'\033[31m',
'limpar':'\033[m',
'magenta':'\033[35m',
'azul':'\033[34m'}

print('{}Bem vindo ao advinhatron 2000 versão 2...{}'.format(cores['magenta'],cores['limpar']))
print('''{}Eu, o computador, vou escolher um numero entre 1 e 10... tente advinhar qual número eu escolhi...{}'''
.format(cores['azul'],cores['limpar']))

print('O computador está escolhendo um número')
for n in range (1,4):
    print ('{}...'.format(n))
    sleep(0.5)
print('PRONTO!')

pc = random.randint(1,10)
tentativas = 0
acertou = False

while not acertou:
    tentativas += 1
    jogador = int(input('Faça seu {} palpite... '.format(tentativas)))
    if jogador == pc:
        print('Você ACERTOU usando {} palpites'.format(tentativas))
        acertou = True
    else:
        if jogador - pc >= 3 or jogador - pc <= -3:
            print('Frio')
        elif jogador - pc >= 2 or jogador - pc <= -2:
            print('Quente')
        elif jogador - pc >= 1 or jogador - pc <= -1:
            print('Muito quente')
        