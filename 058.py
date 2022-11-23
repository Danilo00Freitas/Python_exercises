import random
from time import sleep

cores = {
'verde':'\033[32m',
'vermelho':'\033[31m',
'limpar':'\033[m',
'magenta':'\033[35m',
'azul':'\033[34m'}


print('-=-' * 40)
print('Bem vindo ao advinhatron 2000 versão 2...')
print('Eu, o computador, vou escolher um numero entre 1 e 10... tente advinhar qual número eu escolhi...')
print('-=-' * 40)

num_pc = random.randint(1,10)
num_usr = int(input('Insira um número '))
tentativas = 1

while num_usr > 10 or num_usr < 1:
    print('Escolha um valor de 1 a 10')
    num_usr = int(input('Insira um número '))

if num_usr == num_pc:
    print('''Você {}ACERTOU!{} O número escolhido pela máquina foi {} e
    foram necessárias {} tentativas'''.format(cores['verde'],cores['limpar'],num_pc,tentativas))

while num_usr != num_pc:
    tentativas += 1
    print('Você {}ERROU{}... tente novamente! '.format(cores['vermelho'],cores['limpar']))
    num_usr = int(input('Insira um número '))
    if num_usr == num_pc:
        print('''Você {}ACERTOU!{} O número escolhido pela máquina foi {} e
    foram necessárias {} tentativas'''.format(cores['verde'],cores['limpar'],num_pc,tentativas))





    
