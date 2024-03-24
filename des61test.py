primtermo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
contador = 1
termo = primtermo
print('A progressão aritmética de {} com razão de {} é: '.format(primtermo, razão))
while contador <= 10:
    print('{} -> '.format(termo), end='')
    contador += 1
    termo += razão
print('Fim do programa!')