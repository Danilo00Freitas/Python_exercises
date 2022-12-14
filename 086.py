matriz = list()
temp = list()
cont = 1

print(''' MATRIZ 3x3 vazia.
( A1 ) ( A2 ) ( A3 )
( B1 ) ( B2 ) ( B3 )
( C1 ) ( C2 ) ( C3 )
''')

for c in range(1,10):
    if c <=3:
        x = int(input(f'Insira o elemento A{cont} da Matriz. '))
    elif 6 > c >= 3:
        if c == 4:
            cont = 1
        x = int(input(f'Insira o elemento B{cont} da Matriz. '))
    elif 9 >= c >= 6:
        if c == 7:
            cont = 1
        x = int(input(f'Insira o elemento C{cont} da Matriz. '))
    
    temp.append(x)
    matriz.append(temp[:])
    temp.clear()
    cont += 1
    
for c,n in enumerate(matriz):
    if c == 3 or c == 6:
        print('\n')
    print(f'{n}',end=' ')
    




