dist = float(input('Insira a distância total da viagem... '))

if dist <= 200:
    print('O valor de passagem é de RS{:.2f}'.format(dist * 0.5))
else:
    print('O valor da passagem é de RS{:.2f}'.format(dist * 0.45))

print('Fim.')