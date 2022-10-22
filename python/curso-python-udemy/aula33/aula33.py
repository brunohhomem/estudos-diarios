""""""""""""""""
Dictionary comprehension
"""

lista = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
]

d1 = {x: y for x, y in enumerate(range(5))}
d2 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)
print(d2, '\n',type(d2))