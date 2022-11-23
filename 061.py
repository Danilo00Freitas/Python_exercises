termo = int(input('Insira o primeiro termo '))
razao = int(input('Insira a razão '))
cont = 0

print(termo,end=' -> ')
while cont < 9:
    print(termo + razao,end=' -> ')
    cont += 1
    termo += razao
print('Fim.',end='')


