pessoas = {'Nome': 'Romanelli', 'Sexo': 'M', 'Idade': 22}
#print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos e é do sexo {pessoas["Sexo"]}.')
#? print(pessoas.keys())
#TODO print(pessoas.values())
#!print(pessoas.items())
'''
for k in pessoas.keys():
    print(k)
'''
'''
for k in pessoas.values():
    print(k)
'''
'''
del pessoas['Sexo']             #? Deletar o Valor de alguma key
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''
pessoas['Nome'] = 'Heitor'      #? Trocar o valor de alguma key.
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
'''
pessoas['Peso'] = 85            #? Adicionar uma key nova.
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''