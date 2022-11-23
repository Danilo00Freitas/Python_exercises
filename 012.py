km = float(input('Informe os Km rodados com o carro. '))
t = int(input('Informe o tempo pelo qual o carro foi alugado'))

pmt = 60*t + km*0.15

print('Valor a ser pago:R${:.2f}'.format(pmt))