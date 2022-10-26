"""""""""""""""""
    Considerando duas listas de inteiros ou floats (LISTA A e LISTA B),
some os valores nas listas retornando uma nova lista com os valores somados.

    Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor. 
"""
from itertools import count

index = count()
lista_a = list(range(1, 30, 3))
lista_b = list(range(2, 28, 1))

tam_lista_a = len(lista_a)
tam_lista_b = len(lista_b)

print(f'O tamanho da lista A é: {tam_lista_a}')
print(f'O tamanho da lista B é: {tam_lista_b}')
print()

lista_soma = zip(index, lista_a, lista_b)

for index, lista_a, lista_b in lista_soma:
    print(index, (lista_a + lista_b))
