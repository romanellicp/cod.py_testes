'''while True:
    try:
        num = int(input('Digite um número inteiro: '))
        break
    except ValueError as erro:
        print('Ops o valor digitado não é válido.')
        print('Erro:', erro)
print(f'O valor escolhido foi {num}')
'''
'''
class pessoa:
    def __init__(self, nome, ano_nasc, ano_atual):
        self.nome = nome
        self.idade = ano_atual - ano_nasc


rodolfo = pessoa('Rodolfo', 1986, 2023)
print(rodolfo.nome, rodolfo.idade)
'''
def multiplica(x = 0, y = 0):
    return x * y

n = multiplica(10, 10)
print(n)