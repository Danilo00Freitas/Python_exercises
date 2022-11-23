a = float(input('Insira o primeiro valor: '))
b = float(input('Insira o segundo valor: '))

if a > b:
    print('O númro {} é maior que o número {}'.format(a,b))
elif b > a:
    print('O número {} é maior que o número {}'.format(b,a))
else:
    print('Os dois números são iguais.')