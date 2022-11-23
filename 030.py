numero = int(input('Insira um número... '))

analise = numero % 2

if analise != 0:
    print('O número {} é impar'.format(numero))
else:
    print('O numero {} é par.'.format(numero))

print('Fim')