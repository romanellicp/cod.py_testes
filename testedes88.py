from random import randint
from time import sleep

lista = list()
jogos = list()

quantidade = int(input('Digite a quantidade de jogos: '))
print('          BOA SORTE           ')
sleep(1)
total = 1
while total <= quantidade:
    cont = 0
    while True:
        sorteio = randint(1,60)
        if sorteio not in lista:
            lista.append(sorteio)
            cont += 1
            lista.sort()
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    total += 1
jogos.sort()
print(f'      SORTEANDO {quantidade} JOGOS      ')
sleep(1)
for index, j in enumerate(jogos):
    print(f'JOGO {index+1}: {j}')
    sleep(1)