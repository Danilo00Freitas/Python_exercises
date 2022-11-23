from time import sleep


cores = {
'verde':'\033[32m',
'vermelho':'\033[31m',
'limpar':'\033[m',
'magenta':'\033[35m',
'azul':'\033[34m'}

emprestimo = float(input('Qual o valor da casa que deseja financiar? '))
tempo = float(input('Em quanto tempo deseja pagar? '))
print('Deseja realizar o pagamento em {}{} anos{} ou seja: {}{} meses{}'.format(cores['azul'],
tempo,cores['limpar'],cores['azul'],tempo * 12,cores['limpar']))

salario = float(input('Qual é o seu salário mensal? '))
parcela = float(emprestimo // (tempo * 12))
limite = float((0.3 * salario))
percent_relat = 0.3 - (parcela//salario)

print('Calculando...')
sleep(1)

if parcela >= limite:
    parcela = limite
    tempo_att = emprestimo//parcela 
    print('O empréstimo foi: {}RECUSADO{}'.format(cores['vermelho'],cores['limpar']))
    print('O valor das parcelas é {} superior ao limite'.format(percent_relat)) #TÁ BUGADO!!!!!!!
    print('Na atual condição você pode fazer um empréstimo de até {}R${:.2f}{}'.format(cores['vermelho'],
    limite*(tempo*12),cores['limpar']))
    print('Outra solução é aumentar o tempo de financioamento para {}{} meses{} ou {}{} anos{}'. #SEMI BUGADO!!!!!!
    format(cores['azul'],tempo_att,cores['limpar'],cores['azul'],tempo_att//12,cores['limpar']))
else:
    print('Seu empréstimo foi {}APROVADO{}.'.format(cores['verde'],cores['limpar']))
