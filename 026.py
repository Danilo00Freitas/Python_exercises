frase = str(input('Insira uma frase... ')).strip().upper()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))
print('A última letra "A" aparece na posição {}'.format(frase.rfind('A')+1))

# o comando (R) muda a forma como o programa analisa alguma coisa... neste caso o find procura um valor e retorna ele levando
# em conta o primeiro lugar onde o mesmo apareceu...
# Como ele começa analisando da direira para a esquerda... podemos usar o rfind para mandar começar a procurar da esqueda para direita.
# vale lembrar que a "numeração" dos caracteres não muda... o ultima a no exemplo acima continua estando na 24 casa...
# porém se não fizessemos isso o programa ia sempre parar na segunda casa, onde se localiza o primeiro A.