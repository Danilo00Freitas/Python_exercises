#                           RESOLUÇÃO 1
#sexo = str(input('Insira seu sexo (M/F)')).upper().strip()
#while sexo != 'M' and sexo != 'F':
#    print('Insira o valor M ou F')
#    sexo = str(input('Insira seu sexo (M/F)')).upper().strip()
#print(sexo registrado com sucesso)


#                           RESOLUÇÃO 2
sexo = str(input('Insira o seu sexo (M/F)'))
while sexo not in 'MmFf':
    print('Valor incorreto...')
    sexo = str(input('Insira o seu sexo (M/F)'))
print('Sexo registrado com sucesso!')
