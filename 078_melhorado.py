numeros = list()
maior = menor = 0
c_maior = c_menor = None

for c in range(0,5):
    numeros.append(int(input(f'Insira {c + 1} º número ')))
    if c == 0:
        maior = menor = numeros[c]
        c_maior = c_menor = 1
    else:
        if numeros[c] > maior:
            maior = numeros[c]

        elif numeros[c] < menor:
            menor = numeros[c]

print(f'O maior numero é {maior}, e aparece na posição...',end='')
for i,v in enumerate(numeros):
    if v == maior:
        print(f'{i+1}',end='...')

print(f'\nO menor número é {menor}, e aparece na posição...',end='')
for i,v in enumerate(numeros):
    if v == menor:
        print(f'{i+1}',end='...')

# DESSA FORMA EU DEI USO A FUNÇÃO ENUMARATE... USANDO ELA COM UM LAÇO FOR
# DANDO OUTRA ALTERNATIVA PARA MOSTRAR AS INFORMAÇÕES JUNTO DO PRINT...