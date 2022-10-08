"""""""""""""""""
 - Funções Anônimas - Expressões Lambda
"""

# from random import randint
#
# a = lambda x, y: x * y  # Função anonima, sem nome
#
# for i in range(10):
#     v1 = randint(1, 10)
#     v2 = randint(1, 10)
#     print(f'v1 = {v1} * v2 = {v2} = {a(v1, v2)}')

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# def func(item):
#     return item[1]

# Usar a expressao lambda para simplificar a função
# lista.sort(key=lambda item: item[1], reverse=True)
print(sorted(lista, key=lambda i: i[0], reverse=True))
