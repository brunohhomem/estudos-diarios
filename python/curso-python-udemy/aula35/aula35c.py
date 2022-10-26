# Zip_longest - Itertools - une as duas listas independente do tamanho
# Zip_longest deve ser importado do módulo itertools
from itertools import zip_longest, count

# Código
indice = count()  #Usar o zip_longest com um contador, faz com que o programa conte infinitamente
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(  # Função zip ao inves de zip_longest por que estamos usando indice
    indice,
    estados,
    cidades,
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
