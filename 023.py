from re import M
from unicodedata import ucd_3_2_0


numero = int(input('Informe um número:  '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analisando o número {}'.format(numero))

print('Unidade:{}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

print('Fim.')

# Conseguimos fatiar um numero dividindo o próprio numero pelo múdulo da unidade,dezena etc... 
# Lembrar da aula que fala que 128 é 1*10^2 etc...