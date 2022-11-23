sair = False   
de_maior = de_maior_mulher = h = 0


while sair == False:
    sexo = str(input('Insira seu sexo (M/F): ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Insira seu sexo (M/F): ')).upper().strip()

    idade = int(input('Insira sua idade: '))

    conf = str(input('Deseja continuar? (S/N)')).upper().strip()
    if conf == 'S':
        sair = False
    elif conf =='N':
        sair = True
    else:
        sair = 0
        while sair == 0:
            print('Valor inválido... Tente novamente!')
            conf = str(input('Deseja continuar? (S/N)')).upper().strip()
            if conf == 'S':
                break
            elif conf =='N':
                sair = True
                break
            else:
                sair = 0
    if idade > 18:
        de_maior += 1
    
    if idade > 18 and sexo == 'F':
        de_maior_mulher += 1
    
    if sexo == 'M':
        h += 1

print(f'''
Foram cadastrados {h} homens
Foram cadastrados {de_maior_mulher} mulheres com mais de 20 anos
Foram cadastrados {de_maior} pessoas com mais de 18 anos ''')