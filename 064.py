#parar = False
#cont = 0
#soma = 0
#
#while not parar:
#    ent = int(input('''
#Insira {}º valor
#[999] - SAIR
#Valor --> '''.format(cont)))
#    cont += 1
#    soma += ent
#
#    if ent == 999:
#        cont -= 1
#        soma -= 999
#        parar = True
#
#print('Foram inseridos {} valroes, totalizando {} '.format(cont,soma))


num = cont = soma = 0
num = int(input('Digite um numero de [999] - SAIR '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero de [999] - SAIR '))
print('Você digitou {} numeros e a soma é {}'.format(cont,soma))

#DESSA FORMA QUANDO DIGITO O 999 ELE PARA, JÁ QUE A SOMATÓRIA DA CONTAGEM E SOMA
#ACONTECEM ANTES DO 999 ENCERRAR O PROGRAMA, LOGO NÃO DA TEMPO DE CONTABILZAR