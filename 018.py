import math

ang = float(input('Insira o ângulo desejado '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print('O ângulo {} possui o seno equivalente a {:.2f}'.format(ang,seno))
print('O ângulo {} possui o cosseno equivalente a {:.2f}'.format(ang,cos))
print('O ângulo {} possui a tangente equivalente a {:.2f}'.format(ang,tang))