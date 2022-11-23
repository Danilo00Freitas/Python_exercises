import random  
from time import sleep

verif = False
x = random.randint(1,2)
jog = None
comp = None
result = None
cont = 0

while True:
    if x == 1:
        
        while verif == False:
            jog = str(input('''
Você começa escolhendo!
Par ou Ímpar?
Resposta: ''')).upper().strip()
            
            if jog == 'PAR':
                print('Você escolheu PAR, logo o computador é ÍMPAR!')
                comp = 'ÍMPAR'
                verif == True
                break
            elif jog == 'IMPAR' or jog == 'ÍMPAR':
                print('Você escolheu ÍMPAR, logo o computador é PAR.')
                comp = 'PAR'
                verif == True
                break
            else:
                print('''
Valor inválido''')
                verif == False
    
    else:
        x = random.randint(1,2)
        print('''O computador começa escolhendo...''')
        print('O computador escolheu PAR, logo você é ÍMPAR!' if x == 1 else 'O computador escolheu ÍMPAR, logo você é PAR!')
        if x == 1:
            comp = 'PAR'
        else:
            comp = 'ÍMPAR'

    n_usr = int(input('''
    Qual número você vai jogar?
    Resposta: '''))

    n_cpr = random.randint(1,10)

    if (n_usr + n_cpr) % 2 == 0:
        if jog == 'PAR':
            result = 'você'
        else:
            result = 'o computador'
    else:
        if jog == 'ÍMPAR':
            result == 'você'
        else:
            result = 'o computador'

    print('Par...')
    sleep(1)
    print('ou...')
    sleep(1)
    print('Ímpar...')
    sleep(1)
    print(f'Você jogou o número {n_usr}')
    sleep(1.5)
    print(f'O computador jogou o número {n_cpr}')
    sleep(1.5)

    print(f'O vencedor foi {result}!')
    if result == 'você':
        cont += 1
        if cont == 1:
            print('Parabéns, você venceu 1 vez! O computador quer uma revanche...')
        else:
            print(f'Parabéns, você venceu {cont} vezes! O computador quer mais uma revanche...')
        
    else:
        print('Você perdeu...')
        break