from time import sleep

cores = {
'fecha':'\033[m',
'magenta':'\033[35m',
'azul':'\033[34m',
'verde':'\033[32m'
}

print('-=-'*20)
print('Bem vindo ao analisador de triângulos...')
print('-=-'*20)

A = float(input('Insira o valor do lado A '))
B = float(input('Insira o valor do lado B '))
C = float(input('Insira o valor do lado C '))

print('Analisando...')
sleep(2)

if (A + B) > C and (A + C) > B and (C + B) > A:
    print('Os lados {}A{}, {}B{} e {}C{} PODEM formar um triângulo'.format(cores['magenta'],cores['fecha'],cores['azul'],cores['fecha'],cores['verde'],cores['fecha']))
else:
    print('Os lados A,B e C NÃO PODEM formar um triângulo')