"""""""""
Listas em python
 - Fatiamento
 - append, insert, pop, del, clear, extend, min, max, range
"""

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)  # Estende uma lista com os valores de outra lista

# l2.append('b')  # Insere novo índice ao final de uma lista

l3 = l1 + l2  # Concatena 2 listas

l3.insert(0, 'banana')  # Insere um novo valor no índice indicado.
l3.pop()  # Remove um índice da lista
print(l1)
print(l2)
print(l3)
# print('------------')
# l4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(f'esse é o l4 {l4}')
#
# del(l4[3:5])
# print(f'esse é o l4 {l4}')
#
# print(max(l4))
# print(min(l4))