numeros = (int(input('Primeiro número ')),int(input('Segundo número ')),
int(input('Terceiro número ')),int(input('Quarto número ')))

cont = 0

for n in numeros:
    if n % 2 == 0:
        cont += 1

print(f'Os números escolhidos foram: {numeros}')
print(f'O número 9 foi repetido {numeros.count(9)} vezes')
print(f'O número 3 apareceu primeiro na {numeros.index(3) + 1}º posição')
print(f'Tivemos {cont} numeros pares')
