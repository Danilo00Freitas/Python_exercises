
a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))
c = int(input('Insira o terceiro número: '))

numeros = [a,b,c]

maior_no_momento = None
for numero in numeros:
    if maior_no_momento == None:
        maior_no_momento = numero
    if numero > maior_no_momento:
        maior_no_momento = numero
print('O maior número é {}'.format(maior_no_momento))

menor_no_momento = None
for numero in numeros:
    if menor_no_momento == None:
        menor_no_momento = numero
    if numero < menor_no_momento:
        menor_no_momento = numero
print('O menor Número é {}'.format(menor_no_momento))

print('Fim.')