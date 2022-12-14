numeros = []
cont = p_maior = p_menor = 0
maior = menor = p_maior = p_menor =  None

for n in range(0,5):
    numeros.append(int(input('Insira um número ')))

for n in numeros:
    if cont == 0:
        maior = menor = n
        p_maior = p_menor = 1
        cont += 1 
        
    else:
        if n > maior:
            maior = n
            p_maior += 1
        elif n < menor:
            menor = n
            p_menor += 1
        cont += 1

print(f'''Maior é {maior} na posição {p_maior} 
Menor e {menor} na posição {p_menor}''')


# OPÇÃO COM MENOS LINHAS, PORÉM, MEIO GAMBIARRA...   
        
#numeros.sort()
#print(f'O menor é {numeros[0]} e o maior é {numeros[4]}.')




    

