#                    JEITO FÁCIL
#from math import factorial
#n = int(input('Insira o fatorial desejado... '))
#fat = factorial(n)
#print('O fatorial de {} é {}'.format(n,fat))

#                    JEITO DIFÍCIL

n = int(input('Insira o fatorial desejado... '))

cont = n
fat = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont 
    cont -= 1
print(fat,end='')

#VALE OBSERVAR QUE NESTE EXEMPLO SE TORCAR PARA
# cont -= 1
# fat += cont
# a resolução fica errada por conta de como a matemática vai se comportar...

    

