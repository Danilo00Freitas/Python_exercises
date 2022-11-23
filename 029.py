carro = int(input('Insira a velocidade atual do carro em Km/h... '))

if carro > 80:
    print('Você está acima do limite de velocidade...')
    print('Multa de R$ {:.2f}'.format((carro - 80)*7))

print('Você está dentro da velocidade limite...')
print('FIM')