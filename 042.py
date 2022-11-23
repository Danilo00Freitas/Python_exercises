from time import sleep

cores = {
'fechar':'\033[m',
'vermelho':'\033[31m',
'magenta':'\033[35m',
'azul':'\033[34m',
'verde':'\033[32m'}

print('-=-'*20)
print('Bem vindo ao analisador de triângulos...')
print('-=-'*20)

A = float(input('Insira o valor do lado A '))
B = float(input('Insira o valor do lado B '))
C = float(input('Insira o valor do lado C '))

print('Analisando...')
sleep(2)

if A == B and A != C:
    tipo = '\033[34m ISÓCELES \033[m'
elif A == C and A != B:
    tipo = '\033[34m ISÓCELES\033[m'
elif B == C and B != A:
    tipo = '\033[34m ISÓCELES\033[m'
elif A != B and A != C:
    tipo = '\033[33m ESCALENO\033[m'
else:
    tipo = '\033[32m EQUILÁTERO\033[m'

if (A + B) > C and (A + C) > B and (C + B) > A:
    print('Os lados {}A{}, {}B{} e {}C{} {}PODEM{} formar um triângulo {}'.format(cores['magenta'],cores['fechar'],
    cores['azul'],cores['fechar'],cores['verde'],cores['fechar'],cores['verde'],cores['fechar'],tipo))
else:
    print('Os lados A,B e C {}NÃO PODEM{} formar um triângulo'.format(cores['vermelho'],cores['fechar']))

