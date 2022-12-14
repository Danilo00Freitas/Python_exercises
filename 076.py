lista = ('caderno',20.50,'lapis',1.50,'caneta',3.40)
rep = 1

for item in range (0,len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}',end='') #COMANDO PARA COMPLETAR N CASA DE CARACTER COM ALGUMA COISA A DIREITA.
    else:
        print(f'R${lista[item]: > 5.2f}') #COMANDO PARA COMPLETAR N CASAS DE CARACTERES A DIREITA COM ALGUMA COISA...

