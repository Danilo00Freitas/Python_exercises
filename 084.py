maior = menor = cont = 0
pessoas = []
maior_v = []
menor_v = []
temp = []
while True:
    temp.append(str(input('Insira seu nome ')))
    temp.append(int(input('Insira seu peso ')))
    if cont == 0:
        maior = menor = temp[1]   # Essa resolução funciona, porém, não resolve a possibilidade
        maior_v.append(temp[:])   # de mostrar OS MAIORES PESOS pois se diver dois indivíduos com 
        menor_v.append(temp[:])   # com o mesmo maior peso só vai mostrar um deles...
                                  # uma possível soluao e fazer um programa que salve todos os componenestes em uma lista... 
                                  # analise qual foi o maior peso dentre todos estes componentes e salve em uma variṕavel isolada
                                  # e em seguide compare os valores da lista de pessoas com o valor da variável isolada, e retorne quais foram 
                                  # os maiores e quais foram os menores componentes... 
                                  # segue esta resolução em 084_melhorado.py
    else:
        if temp[1] > maior:
            maior = temp[1]
            maior_v.pop()
            maior_v.append(temp[:])

        elif temp[1] < menor:
            menor = temp[1]
            menor_v.pop()
            menor_v.append(temp[:])

    temp.clear()
    cont += 1
    x = str(input('Deseja continuar? [S/N] '))
    if x in 'Ss':
        print('continuando...')
    elif x in 'Nn':
        break

print(f'Foram cadastradas {cont} pessoas')
print(f'A pessoa mais pesada pesa {maior} Kgs e mais leve {menor} Kgs')
print(f'Maior valor {maior_v}')
print(f'Menor valor {menor_v}')


