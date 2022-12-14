numeros = list()
cont = 1

while True:

    add = int(input(f'Forneça o {cont}º número '))
    if add in numeros:
        print('Número já consta na lista')
    else:
        numeros.append(add)
        cont += 1
        
    sair = str(input('Deseja continuar? (S/N) '))

    if sair in 'Nn':
        break 

    elif sair in 'Ss':
        print('Continuando...')

    else:
        print('erro!')
        sair = str(input('Deseja continuar? (S/N) '))



print('Foram adicionados a lista os itens: ',end=' ')
numeros.sort()
for n in numeros:
    print(n,end=' ... ')


    


    


