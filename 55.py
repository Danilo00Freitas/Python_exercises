menor_p = None
maior_p = None

for pessoas in range (0,5):
    peso = float(input('Insira o seu peso. '))
    if maior_p == None or menor_p == None:
        menor_p = peso
        maior_p = peso
       
    else: 
        if peso > maior_p:
            maior_p = peso
        
        elif peso < menor_p:
            menor_p = peso
        
print('Maior = {}'.format(maior_p))
print('Menor = {}'.format(menor_p))

# outra forma seria colocando a condição de que caso seja o primeiro ciclo do looping, o valor passa de zero ao primeiro valor que foi digitado no input do loop.
