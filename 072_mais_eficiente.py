numeros = ('um','dois','três','quatro','cinco','seis','sete'
,'oito','nove','dez','onze','doze','treze','quatorze','quinze'
,'dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    nmr = int(input('Qual número deseja mostrar? ')) -1
    if 0 <= nmr <= 19:
        print(f'O número escolhido foi {numeros[nmr]}')
        break
    print('Digite um valor válido')

