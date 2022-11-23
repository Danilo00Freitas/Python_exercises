frase = str(input('Insira uma frase... ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
tamanho = len(junto)
inverso = ''
print(junto)

for letras in range((tamanho-1),-1,-1):
    inverso += junto[letras] # com isso o inverso vai ir se tornando meio que uma soma de caracteres... pega oque tinha soma... pega oque virou e soma

print('{} invertido fica {}'.format(junto,inverso))

if junto == inverso:
    print('E por isso TEMOS um palíndromo...')
else:
    print('Por isso NÃO TEMOS um palíndromo...')
