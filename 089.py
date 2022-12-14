temp = list()
notas = list()
cont = 1
nomes = ['NO','NOME','MÉDIA']

while True:
    nome = str(input(f'Insira o nome do {cont} aluno. '))
    nota_1 = int(input('Insira a primeira nota. '))
    nota_2 = int(input('Insira a segunda nota. '))
    print()
    media = (nota_1 + nota_2) // 2 

    temp.append(nome)
    temp.append(nota_1)
    temp.append(nota_2)
    temp.append(media)
    notas.append(temp[:])
    temp.clear()
    cont += 1

    x = str(input('Deseja continuar? [S/N] '))
    if x in 'Ss':
        print('Continuando...')
        print()
    elif x in 'Nn':
        print('-=-'*40)
        break

for c in range(0,len(notas)):
    if c == 0:
        for n in nomes:
            print(f'{n:^10}',end='')
        print('\n')

    print(f'{c:^10}',end='')
    print(f'{notas[c][0]:^10}',end='')
    print(f'{notas[c][3]:^10}',end='')
    print()

while True:
    aluno = int(input('Deseja ostrar a nota de qual aluno? (999 --> SAIR) '))
    if aluno == 999:
        break
    print(f'''
O aluno selecionado foi: {notas[aluno][0]
    }
Nota da primeira prova {notas[aluno][1]}
Nota da segunda prova {notas[aluno][2]}''')
    print()

    

    