cores = {
'fechar':'\033[m',
'vermelho':'\033[31m',
'magenta':'\033[35m',
'azul':'\033[34m',
'verde':'\033[32m'}


print('='*25)
print('   LOJAS PEGANA JEBA')
print('='*25)

preço = float(input('Insira o preço do produto desejado... '))
pmt = int(input('''
Qual a forma de pagamento?
[1] a vista/cheque: 10% de desconto
[2] débito a vista (cartão): 5% de desconto
[3] parcelamento 2x: preço normal
[4] parcelamento 3x ou mais: 20% de juros '''))

if pmt == 1:
    p_final = 0.9 * preço
    desconto = 0.1 * preço
    print('''valor da compra: {}R${:.2f}{}
    Desconto total de: {}R${:.2f}{}'''.format(cores['azul'],p_final,cores['fechar'],cores['verde'],desconto,cores['fechar']))

elif pmt == 2:
    p_final = 0.95 * preço
    desconto = 0.05 * preço
    print('''valor da compra: {}R${:.2f}{}
    Desconto total de: {}R${:.2f}{}'''.format(cores['azul'],p_final,cores['fechar'],cores['verde'],desconto,cores['fechar']))

elif pmt == 3:
    print('''valor da compra: {}R${:.2f}{}.
    O pagamento será ralizado em duas parcelas de {}R${:.2f}{}'''.format(cores['azul'],preço,cores['fechar'],
    cores['verde'],preço // 2, cores['fechar']))

elif pmt == 4:
    parcelas = float(input('Quantas parcelas? '))
    p_final = (preço // parcelas) * 1.2
    p_total = p_final * parcelas
    print('''Valor do produto {} R${:.2f}{}.
    Preço atualizado com o parcelamento: {}R${:.2f}{}.
    O produto será pago em {}{} parcelas{} de {}R${:.2f}{}.'''.format(cores['azul'],preço,cores['fechar'],
    cores['magenta'],p_total,cores['fechar'],cores['verde'],parcelas,cores['fechar'],cores['verde'],p_final,cores['fechar']))

else:
    print('{}Escolha uma opção válida entre 1 e 4.{}'.format(cores['vermelho'],cores['fechar']))

print('FIM.')