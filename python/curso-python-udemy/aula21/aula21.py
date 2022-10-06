""""""""""
For / Else
"""

lista = ['bruno', 'henrique', 'thor', 'doctor', 'jones']
comeca_com_b = False

for valor in lista:
    if valor.startswith('b'):
        comeca_com_b = True
else:
    print('Não tem palavra que começa com b')