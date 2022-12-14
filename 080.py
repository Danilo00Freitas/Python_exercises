numeros = []

for r in range(0,5):
    val = int(input('Insira um número '))
    if r == 0 or val > numeros[-1]: # ---> indicando que estou pegando o ultimo elemento adicionado... seria a mesma coisa que fazer lista[len.(lista)-1]
        numeros.append(val)
    else:
        pos = 0
        while pos < len(numeros):
            if val <= numeros[pos]:
                numeros.insert(pos,val)
                break
            pos += 1

print(numeros)

# INTERESSANTE REVISAR ESTE CÓDIGO...