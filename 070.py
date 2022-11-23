qtd_prods = 1
sair = False     
total = 0
maior_mil = 0
mais_caro = 0   
rep = 0

while sair == False:
    prod = str(input(f'Qual o nome do {qtd_prods} produto? '))
    qtd_prods += 1
    preço = int(input('Qual o preço deste produto? '))
    if preço > 1000:
        maior_mil += 1
    total += preço
    if preço > mais_caro:
        mais_caro = preço
    deseja_sair = str(input('Deseja continuar? (S/N)')).upper().strip()
    if deseja_sair == 'N':
        sair == True
    else:
        sair == False
        break

print(f'''
O total gato foi de R${total},00
O produto mais caro custou R${mais_caro},00
{maior_mil} produtos custaram mais de R$1000,00''')