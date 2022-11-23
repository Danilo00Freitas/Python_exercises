n1 = float(input('Insira a primeira nota '))
n2 = float(input('Insira a segunda nota '))
med = (n1+n2)//2

if med < 5.0:
    status = '\033[31m REPROVADO'
elif med > 5.0 and med < 7:
    status = '\033[33m RECUPERAÇÃO'
else:
    status = '\033[32m APROVADO'

print('''A sua média foi {}.
Você está {}'''.format(med,status))

