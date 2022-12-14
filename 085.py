numeros = [[],[]]

for c in range(0,7):
    x = int(input('Insira um número '))

    if x % 2 == 0:
        numeros[0].append(x)
    elif x % 2 == 1:
        numeros[1].append(x)

print(sorted(numeros[0])) #--> PODERIA USAR numeros[0].sort()
print(sorted(numeros[1])) #-->  PODERIA USAR numeros[1].sort()