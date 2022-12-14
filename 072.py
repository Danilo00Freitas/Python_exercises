numeros = ('um','dois','três','quatro','cinco','seis','sete'
,'oito','nove','dez','onze','doze','treze','quatorze','quinze'
,'dezesseis','dezessete','dezoito','dezenove','vinte')

usr = int(input('Escolha um numero de 1 a 20: ')) - 1
while True:
    if 0 <= usr <=20: 
        print(f'O número escolhido foi {numeros[usr]}')
        break
    else:
        'Valor inválido... selecione novamente'
        usr = int(input('Escolha um numero de 1 a 20: ')) - 1