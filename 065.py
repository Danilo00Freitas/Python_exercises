stop = False
soma = 0
maior = None
menor = None
cont = 0

n = int(input('Insira um valor '))
while not stop:
    soma += n

    if cont == 0:
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    c = str(input('Deseja continuar? (S/N): ')).upper().strip()
    if c == 'N':
        stop = True
    elif c == 'S':
        n = int(input('Insira um valor '))
    else:
        c = str(input('Opção inválida... Deseha continuar? (S/N): ')).upper().strip()
    
    cont += 1
        
media = soma/cont
print('''
Maior número: {}
Menor número: {}
média:{}'''.format(maior,menor,media))