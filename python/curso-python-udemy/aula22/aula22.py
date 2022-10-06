"""""""""""
Split, Join, e Enumerate
 - Split - Dividir uma string
 - Join - Junta uma lista
 - Enumerate - Enumera elementos da lista 
"""

string = 'O Brasil é penta'
lista = string.split(' ')  # Separou a string nos espaços
# string2 = '_'.join(lista)  # Costurou a string usando underlines '_'
#
# print(string)
# print('------------')
# print(lista)
# print('------------')
# print(string2)

for indice, valor in enumerate(lista):
    print(indice, valor)

