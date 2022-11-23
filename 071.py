saque = int(input('Quantos reais você deseja sacar? '))
caixa = saque
cedula = 50
tot_ced = 0

while True:
    if caixa >= cedula:
        caixa -= cedula
        tot_ced += 1
    else:
        print(f'Foram usasdas {tot_ced} cédulas de {cedula}.')
        tot_ced = 0
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        if caixa == 0:
            break
