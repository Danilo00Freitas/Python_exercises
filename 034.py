print('-=-'*30)
print('Insira seu salário atual')
salario = float(input('Atualmente recebo R$ '))
print('-=-'*30)

cores = {
'fecha':'\033[m',
'azul':'\033[34m',
'ciano':'\033[36m',
'verde claro':'\033[92m'
}


if salario <= 1250:
    salario_att = salario * 1.15
    print('Seu novo salário será R$ {}{:.2f}{} tendo recebido um aumento de {}15%{}'.format(cores['azul'],salario_att,cores['fecha'],
cores['verde claro'],cores['fecha']))
else:
    salario_att = salario * 1.1
    print('Seu novo salário será R$ {}{:.2f}{} tendo recebido um aumento de {}10%{}'.format(cores['ciano'],salario_att,cores['fecha'],
cores['verde claro'],cores['fecha']))
 
print('Fim.')
