# d1 = {'chave1': 'valor da chave'}
# d1['nova_chave'] = 'Valor da nova chave'
#
# d2 = dict(chave1='valor da chave1', chave2='valor da chave2')
#
# print(d1)
# print(d1['chave1'])
# print(d2)

d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'tupla',
    'cliente3': {
        'nome': 'Vitória',
        'sobrenome': 'Soares',
    },
}


print(d1[(1, 2, 3, 4)])
print('Destá, eu eu de ver você batendo em minha porta')
print('toc toc toc')