soma = 0
contador = 0
for numero in range(1,501,2):
    if numero % 3 == 0:
        contador = contador + 1 # como isso é um contador ele vai recebendo 1 em 1 para contar quantas vezes algo se repetiu...
        # ISSO ACONTECE PORQUE ESTÁ DENTRO DO LOOP CONDICIONAL DE SER MÚLTIPLO DE 3... SE ESTIVESSE FORA IRIA CONTAR QUANTAS NUMEROS EXISTEM DE 1 A 501 DE 2 EM 2..
        #OU SEJA QUANTOS NÚMEROS ÍMPARES...
        soma = soma + numero # como isso é um acumulador ele vai somando os números que foram encontrados... 
print('A soma de todos os números multiplos de 3 é {}... ao total foram somados {} numeros'.format(soma,contador))


# CONTADOR = CONTADOR + 1 PODE SER SIMPLIFICADO PARA CONTADOR += 1