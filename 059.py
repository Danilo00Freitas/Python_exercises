from time import sleep

sair = False
certo = False

possivel = [1,2,3,4,5]

v1 = int(input('Insira o primeiro valor '))
v2 = int(input('Insira o segundo valor '))

while not sair:
    opr = int(input('''
    -------------MENU--------------
    Qual operação deseja realizar?

    [1] - Somar
    [2] - Multiplicar
    [3] - Maior (Comparação lógica)
    [4] - Novos números (Atualizar)
    [5] - sair

    Operação desejada: '''))
    
    if opr == 5:
        print('Encerrando...')
        sleep(2)
        sair = True
        
    elif opr == 1:
        print('''
Você escolheu a operação SOMA. 
A soma de v1({}) com v2({}) resulta no número {}'''.format(v1,v2,v1+v2))
    
    elif opr == 2:
        print('''
Você escolheu a operação MULTIPLICAR. 
A multiplicação de v1({}) com v2({}) resulta no número {}'''.format(v1,v2,v1*v2))
    
    elif opr == 3:
        maior = None
        if v1 > v2:
            maior = v1
        elif v2 < v1:
            maior = v2
        else:
            maior = 'Mesmo valor'
        print('''
Você escolheu a operação MAIOR (COMPARAÇÃO LÓGICA).
Entre os valores v1({}) e v2({}) o maior é {}'''.format(v1,v2,maior))
        
    elif opr == 4:
        print('''
Você escolheu a operação NOVOS NÚMEROS (ATUALIZAR).''')
        att = int(input('''
        ----------------MENU ATT------------------
        Informe quais números deseja atualizar
        [1] - v1
        [2] - v2
        [3] - AMBOS
        Selecione: '''))
        if att == 1:
            v1 = int(input('Insira o novo v1 '))
        elif att == 2:
            v2 = int(input('Insira o novo v2 '))
        elif att == 3:
            v1 = int(input('Insira o novo v1 '))
            v2 = int(input('Insira o novo v2 '))
    else:
        print('Opção inválida... selecione novamente!')

    

        



