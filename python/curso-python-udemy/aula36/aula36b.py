"""""""""""""""""""""""""""""""""
Combinations, permutations e product - Itertools
Combinação = Ordem não importa;
Permutação = Ordem importa;
* Ambos não repetem valores únicos *
Produto = Ordem importa e repete valores únicos.
"""
from itertools import combinations, permutations, product

pessoas = ['Bruno', 'Vitória', 'Butters', 'Hermione']

for grupo in product(pessoas, repeat=2):
    print(grupo)
