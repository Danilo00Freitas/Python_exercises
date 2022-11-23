cores = {
'limpar':'\033[m',
'verde':'\033[32m',
'azul':'\033[34m',
'vermelho':'\033[31m',
'amarelo':'\033[33m',
'magenta':'\033[35m',
'ciano':'\033[36m'}

print('{}-=-{}'.format(cores['magenta'],cores['limpar'])*14)
print('       {}Progressão aritimética v3.0{}'.format(cores['azul'],cores['limpar']))
print('{}-=-{}'.format(cores['magenta'],cores['limpar'])*14)

termo = int(input('Insira o primeiro termo '))
razao = int(input('Insira a razão '))
rep = 0
rep_a_mais = 10
cont = 1

while rep_a_mais != 0:
    rep += rep_a_mais
    while cont <= rep:
        print('{} -> '.format(termo),end='')
        termo += razao
        cont += 1
    print('{}PAUSA{}'.format(cores['vermelho'],cores['limpar']))
    rep_a_mais = int(input('Quantas repetições a mais deseja fazer? '))

print('Progressão finalizada. Foram mostrados {} termos da progressão.'.format(cont))

