"""""""""""""""""""""""
Caso 1 - Dobrar o valor de um produto.
Caso 2 - Todos os produtos que custam acima de 1000, imposto de 50% sobre o valor total.

"""

lista_precos = [500, 1000, 1500, 2000, 120, 50, 300, 997]

# Fazendo com for in
nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco*2)

print(nova_lista_precos)

nova_lista_precos2 = [preco * 2 for preco in lista_precos]
print(nova_lista_precos2)

imposto = []
for preco in lista_precos:
    if preco > 1000:
        imposto.append(preco * 0.5)
print(imposto)

imposto2 = [preco * 0.5 for preco in lista_precos if preco > 1000]
print(imposto2)