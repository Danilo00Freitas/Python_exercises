usuario = int(input('Informe o número desejado '))
cont = None
accm = 0

for numeros in range(-1,9):
    if cont == None:
        cont = 0
        accm += usuario
        print('{} x {} = {}'.format(usuario,cont,usuario*cont))
    cont += 1
    accm += usuario
    print('{} x {} = {}'.format(usuario,cont,usuario*cont))
