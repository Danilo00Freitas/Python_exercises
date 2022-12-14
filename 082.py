numeros = []
pares = []
impares = []
while True:
    numeros.append(int(input('Insira um núemro ')))
    x = str(input('Continuar? [S/N] '))
    if x in 'Ss':
        print('Continuando...')
    elif x in 'Nn':
        break

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista completa {numeros}')
print(f'PARES {pares}')
print(f'ÍMPARES{impares}')