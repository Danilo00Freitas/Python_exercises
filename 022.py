nome_completo = str(input('Informe seu nome completo___')).strip()
print('Analisando seu nome...')

print('Seu nome em letras maiúsculas fica {}'.format(nome_completo.upper()))
print('Seu nome em letras minúsculas fica {}'.format(nome_completo.lower()))
print('Seu nome possui {} letras'.format(len(nome_completo) - nome_completo.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome_completo.find(' '))) 
#isso vai funcionar de forma pontual...
separa = nome_completo.split()
print('Seu primeiro nome tem {} letas'.format(len(separa[0])))