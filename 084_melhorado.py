maior = menor = cont = 0

pessoas = []
temp = []

while True:
    temp.append(str(input('Insira seu nome ')))
    temp.append(int(input('Insira seu peso ')))
    if cont == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]

        elif menor > temp[1]:
            menor = temp[1]
    cont += 1
    pessoas.append(temp[:])
    temp.clear()
    x = str(input('Deseja continuar? [S/N] '))
    if x in 'Ss':
        print('Continuando...')
    elif x in 'Nn':
        break


print(f'Foram analisadas {cont} pessoas.')
print(f'O menor peso foi {menor} Kg... as seguintes pessoas possuem este peso: ',end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0],end=', ')
print(f'\nO maior peso foi {maior} Kg... as seguintes pessoas possuem este peso: ',end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0],end=', ')

#                        PRECISO LEMBRAR QUE NEM SEMPRE PRA RESOLVER UMA LISTA
#                        EU PRECISO ADICIONAR OS ELEMENTOS EM UMA LISTA...
#                        NESTE CASO EU MOSTREI OS RESULTADOS USANDO PRINT
#                        COMPARANDO OS VALORES DA LISTA COM O MAIOR E O MENOR
#                        E NÃO NECESSARIAMENTE SEPAREI EM DUAS LISTAS COM OS MAIORES
#                        E COM OS MENORES