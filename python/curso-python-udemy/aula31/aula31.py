""""""""""""""""
    Sets (Conjuntos) em python
    - Uma coleção de elementos
    
    add, update, clear, discard
    union | (une)
    intersection & (todos os elementos presentes nos dois sets) 
    difference - (elementos apenas no set da esquerda)
    symmetric_difference ^ (elementos que estão nos dois sets mas não em ambos) 
"""
# há duas maneiras de criar sets

# s1 = {1, 2, 3, 4, 5}  # Similar a criação de um dicionario, mas set n precisa de chave
#
# print(s1)
# s1.add(6)
# print(s1)
# s1.discard(3)
# print(s1)
# s1.update('Bruno')
# print(s1)

# Lista, transforma em set para remover valores duplicados dps volta a ser lista, agora sem valor duplicado.
lista = [1, 1, 2, 3, 1, 3, 4, 5, 6, 2, 3, 5, 6, 4, 1, 2, 3]  # lista com valores duplicados
print(f'Lista com valores duplicados:\n{lista}')
lista = set(lista)
print(f'Transformando a lista em um set e removendo valores duplicados:\n{lista}')
lista = list(lista)
print(f'Voltando a lista pro seu tipo normal, sem valores duplicados:\n{lista}')
