from random import randint
maior = 0
menor = 1000

numeros = (randint(1,999),randint(1,999),randint(1,999)
,randint(1,999),randint(1,999))

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    
    
print(f'Os números sorteador foram {numeros}')
print(f'O maior número foi {maior} e o menor número foi {menor}')
