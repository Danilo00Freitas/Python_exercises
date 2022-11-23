import math

cat = float(input('Insira o valor do cateto oposto '))
cat_op = float(input('Insira o valor do cateto adjacente '))
hipot = math.hypot(cat,cat_op)

print('A hipotenusa vai medir {:.2f}'.format(hipot))
