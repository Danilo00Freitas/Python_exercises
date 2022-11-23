idade =  int(input('Informe a sua idade '))

if idade <= 9:
    categoria = '\033[32mMIRIM'

elif idade <= 14:
    categoria = '\033[32mINFANTIL'

elif idade <= 19:
    categoria = '\033[32mJÚNIOR'

elif idade <= 25:
    categoria = '\033[32mSÊNIOR'

else:
    categoria = '\033[32mMASTER'

print('A sua categoria é: {}'.format(categoria))