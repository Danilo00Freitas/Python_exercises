nome = str(input('Insira seu nome completo:  ')).strip().title()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))

# o comando len também nos informa a quantidade de itens em uma lista...
