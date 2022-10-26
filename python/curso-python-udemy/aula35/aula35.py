""""""""""""""""""""""
Zip - Unindo iteráveis (une até o tamanho máximo da menor das listas)
Zip_longest - Itertools
"""

# Código
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)  # Função zip juntou as duas listas.
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

for valor in cidades_estados:
    print(valor[0], valor[1])
