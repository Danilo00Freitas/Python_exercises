
n = int(input('Informe quantos termos deseja ver... '))
cont = 1
    
n1 = 1
n2 = 0
n3 = n1 + n2

#print('{} -> {} ->'.format(n1,n2),end='')
while cont <= n:
    print('{} -> '.format(n3),end='')
    cont += 1
    n1 = n2
    n2 = n3
    n3 = n1 + n2

print('Fim.')







