acc = None
cont = 0
for n in range(0,6):
    num = int(input('Insira um número...'))
    if acc == None:
        acc = 0
    if num % 2 == 0:
        acc += num
        cont += 1
        print('O número {} é PAR'.format(num))
print('A soma dos {} números PARES é {}'.format(cont,acc))