resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Você quer continuar? [S/N]: ')).upper().strip()
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print(f'O maior número é {maior} e o menor número é {menor}')
print(f'Você digitou {quant} valores e a média entre eles é {media}')
print('Acabou')
