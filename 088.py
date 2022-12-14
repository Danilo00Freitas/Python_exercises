import random
from time import sleep
mega = []
temp = []
c = 0
print()
print('-='*10,end='')
titulo = 'BEM VINDO AO SIMULADOR DE MEGA SENA'
print(f'{titulo}',end='')
print('=-'*10)

sleep(2)

x = int(input('Informe a quantidade de jogos: '))

sleep(2)

for c in range(0,x):
    for n in range(0,6):
        if n == 0:
            temp.append(random.randint(0,60))
        else:
            x = random.randint(0,60)
            while x in temp:
                x = random.randint(0,60)
            temp.append(x)
    temp.sort()
    mega.append(temp[:])
    temp.clear()

for e in range(0,len(mega)):
    print(f'{e + 1}º palpite: {mega[e]}')
    print()
    sleep(0.5)

print('FIM.')


