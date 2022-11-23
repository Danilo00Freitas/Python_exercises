cores = {
'verde':'\033[32m',
'vermelho':'\033[31m',
'limpar':'\033[m',
'magenta':'\033[35m',
'azul':'\033[34m'}

print('-=-'*30)
print('Bem vindo ao {}conversor de medidas{}...'.format(cores['magenta'],cores['limpar']))
print('-=-'*30)

num = int(input('Forneça o número que deseja converter... '))
escolha = int(input('''Escolha uma das bases para conversão...
[1] para binário
[2] para octal
[3] para hexadecimal
escolha:  '''))

if escolha == 1:
    print('O número {}{}{} convertido em {}binário{} é: {}{}{}'.format(cores['azul'],num,cores['limpar'],cores['magenta'],
    cores['limpar'],cores['verde'],bin(num)[2:],cores['limpar']))
elif escolha == 2:
    print('O número {}{}{} convertido em {}octal{} é: {}{}{}'.format(cores['azul'],num,cores['limpar'],cores['magenta'],
    cores['limpar'],cores['verde'],oct(num)[2:],cores['limpar']))
elif escolha == 3:
    print('O número {}{}{} convertido em {}hexadecimal{} é: {}{}{}'.format(cores['azul'],num,cores['limpar'],cores['magenta'],
    cores['limpar'],cores['verde'],hex(num)[2:],cores['limpar']))
else:
    print('VOCÊ É BURRO MANO?')
    exit()

print('Fim.')
exit