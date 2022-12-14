palavras = ('mamadeira','macaco','buzina','girafa','pedreiro',
'corneta','maçaneta','dinossauro')

for palavra in palavras:
    print(f'\nA palavra {palavra} contém ',end='') #COMANDO PARA QUEBERAR O TEXTO...
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra,end=' ')

#COMO CADA PALAVRA INDIVIDUAL É UMA LISTA DE LETRAS EU POSSO USAR FOR LETRA IN PALAVRA...
# PARA CADA FOR FOR ESPECIFICANDO UMA UNIDADE DE MEDIDA O PYTHON VAI TRABALAHDNO MAIS PROFUNDAMENTE