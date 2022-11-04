from dados import produtos, pessoas, lista

# print(lista)
# nova_lista = map(lambda x: x * 10, lista)  # multiplicando cada item da lista importada, utilizando a função map
# nova_lista2 = [x * 2 for x in lista]
# print(list(nova_lista))
# print(list(nova_lista2))

precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)
