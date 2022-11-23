from datetime import date
data_atual = date.today().year
print(data_atual)
cont_maior = 0
cont_menor = 0

for datas in range (0,7):
    nascimento = int(input('Insira o ano do seu nascimento...'))
    if data_atual - nascimento >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print('Temos {} maiores de idade e {} menores de idade.'.format(cont_maior,cont_menor))

        
