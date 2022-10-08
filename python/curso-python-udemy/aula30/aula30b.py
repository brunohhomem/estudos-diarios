# Dicionarios dentro de dicionarios

clientes = {
    'cliente1': {
        'nome': 'Bruno',
        'sobrenome': 'Homem',
    },
    'cliente2': {
        'nome': 'Butters',
        'sobrenome': 'Homem',
    },
    'cliente3': {
        'nome': 'Vitória',
        'sobrenome': 'Soares',
    },
    'cliente4': {
        'nome': 'Elias',
        'sobrenome': 'Alberto',
    },
}

# Iteracao de dicionario dentro de dicionario
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


