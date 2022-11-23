
numero = int(input('insira um número '))

for n in range(2, numero):
    valor = 'PRIMO'
    teste = numero % n
    if teste == 0:
        valor = 'NÃO PRIMO'
        break
print('O número {} é : {}'.format(numero,valor))





