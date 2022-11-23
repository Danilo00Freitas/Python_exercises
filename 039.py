import datetime 

cores = {
'verde':'\033[32m',
'vermelho':'\033[31m',
'limpar':'\033[m',
'magenta':'\033[35m',
'azul':'\033[34m'}


ano_at = datetime.date.today().year

idade = int(input('Qual é a sua idade? '))
print('Você tem {}{} anos{}'.format(cores['verde'],idade,cores['limpar']))

dt_nascimento = ano_at - idade
print('Você nasceu em {}{}{}'.format(cores['verde'],dt_nascimento,cores['limpar']))

if idade == 18:
    print('Você {}PRECISA SE ALISTAR{} este ano ({}{}{})'.format(cores['vermelho'],
    ['limpar'],cores['vermelho'],ano_at,cores['limpar']))

elif idade < 18:
    alist_fut = (18 - idade) + ano_at
    print('''
    Você {}NÃO TEM 18 ANOS{}.
    Seu alistamento está previsto para {}{}{}.
    Faltam {}{} anos para o seu alistamento.{}'''.format(cores['vermelho'],cores['limpar'],
    cores['verde'],alist_fut,cores['limpar'],cores['verde'],18 - idade,cores['limpar']))

else:
    alist_pas = ano_at - (idade - 18) 
    print('''Seu alistamento {}ESTÁ ATRASADO{}.
     Você deveria ter se alistado em {}{}{}.
     Seu alistamento está {}{} anos{} atrasado.'''.format(cores['vermelho'],cores['limpar'],
    cores['verde'],alist_pas,cores['limpar'],cores['vermelho'],idade - 18,cores['limpar']))

print('Fim.')


