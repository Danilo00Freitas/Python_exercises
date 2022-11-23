#NO PYTHON NÃO TEMOS A ESTRUTURA DO WHILE... MAS PODEMOS REPRODUZIR O MESMO EFEITO.
#Quando falamos por exemplo
#x = 1                       
#while x <= 10:
#    print(x, ' -> ',end='')
#    x += 1
#print('Acabou')  
#   Quando falamos isso é a mesma coisa que dizer que enquanto x <= 10 == True
#   LOGO PODEMOS USAR WHILE TRUE, WHILE FALSE... PORÉM DESSA FORMA O PROGRAMA VAI CORRER PARA SEMPRE
#   Para parar a execução infinita usamos BREAK
s = c = 0
while True:
    n = int(input('Insira um número '))
    if n == 999:
        break
    c += 1
    s += n
print('Foram inserisos {} valores e a soma é {}'.format(c,s))
                        # USANDO UMA fstring
print(f'Foram inseridos {c} valores e a some é {s}')