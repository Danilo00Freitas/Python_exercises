numeros = []
cont = 0
while True:
    numeros.append(int(input('Insira um número ')))
    cont += 1
    x = str(input('Deseja continuar? (S/N)'))
    if x in 'Nn':
        break
    elif x in 'Ss':
        print('Continuando...')

print(f'Foram digitador {cont} valores')
if 5 in numeros:
    print('O número 5 está presente')
else:
    print('O número 5 não está presente')

print(numeros.sort(reverse = True))