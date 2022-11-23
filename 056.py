soma_idade = 0
idade_media = ''
idade_tot = 0
hmv = None
nome_hmv = ''
cont_mulher = None

for pessoa in range (1,5):
    print('____ pessoa {}____'.format(pessoa))
    nome = str(input('Insira seu nome: ')).title().strip()
    sexo = str(input('Insira seu sexo [M/F]: ')).strip().upper()
    idade = int(input('Insira a sua idade: '))
    soma_idade += idade
    if pessoa == 1 and sexo == 'M':
        hmv = idade
        nome_hmv = nome
    if sexo == 'M' and idade > hmv:
        hmv = idade
        nome_hmv = nome

    if cont_mulher == None:
        cont_mulher = 0
    if sexo == 'F' and idade < 20:
        cont_mulher += 1


idade_media = float(soma_idade / 4)            
     
print('A médias das idades do grupo é {} anos'.format(idade_media))

print('O homem mais velho se chama {} e tem {} anos.'.format(nome_hmv,hmv))

if cont_mulher > 1:
    print('Temos {} mulheres com menos de 20 anos.'.format(cont_mulher))
else:
    print('Temos {} mulher com menos de 20 anos'.format(cont_mulher))