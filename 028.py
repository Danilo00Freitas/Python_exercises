import random
from time import sleep
print('-=-' * 40)
print('Bem vindo ao advinhatron 2000...')
print('Eu, o computador, vou escolher um numero entre 1 e 5... tente advinhar qual número eu escolhi...')
print('-=-' * 40)

num_pc = random.randint(1,5)

num_user = int(input('Insira um número de 1 a 5...  '))

if num_user > 5:
    print('O número {} não atende o critério'.format(num_user))
    quit()
elif num_user < 1:
    print('O número {} não atende o critério'.format(num_user))
    quit()

print('PROCESSANDO...')
sleep(2)

if num_user == num_pc:
    print('Você acertou... o número escolhido foi {}'.format(num_pc))
else:
    print('Você errou... Você escolheu {} e o correto seria {}'.format(num_user,num_pc))
print('FIM')

