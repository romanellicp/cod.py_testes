from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolhe PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'O Jogador escolheu {jogador} e o computador escolheu {computador} e o total foi {total}!')
    print('DEU PAR!!!' if total % 2 == 0 else 'DEU IMPAR!!!')
    if tipo == 'P':
        print('Você jogou PAR')
        if total % 2 == 0:
            print('Você GANHOU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        print('Você jogou IMPAR!')
        if total % 2 == 1:
            print('Você GANHOU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Você ganhou {vitoria} vezes!')