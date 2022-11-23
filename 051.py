termo = int(input('Insira o primeiro termo '))
razao = int(input('Insira a razão '))

print(termo,end=' -> ')
for n in range(0,9):
    termo += razao
    print(termo,end= ' -> ')
print('ACABOU')


