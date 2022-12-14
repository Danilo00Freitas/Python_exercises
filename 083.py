ex = str(input('Insira a sua expressão matemática '))

lista = []

for c in ex:
    if '(' in c:
        lista.append('(')

    elif ')' in c:
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')') 

if len(lista) == 1:
    print('A expressão está incorreta... ')
elif len(lista) == 0:
    print('A expressão está correta ')
else:
    print('ERRO!!')









# SEGUNDO ESTA LÓGICA... SEMPRE QUE A EXPRESSÃO ESTIVER ERRADA O LEN VAI SER MAIOR QUE UM,
# POIS NÃO VAI TER PARENTESES O SUFICIENTE PARA DAR POP E FECHAR A CONTA EM ZERO...