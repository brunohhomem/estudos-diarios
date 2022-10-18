""""""""""""""""
Dictionary comprehension
"""

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
]

d1 = {x.upper(): y.upper() for x, y in lista}
print(d1)
