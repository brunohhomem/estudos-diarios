""""""""""""""""
List comprehension
- Otimização (performance do código)
- Escrever menos linhas de código.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisao = [numero / 2 for numero in numeros]  # fazendo um for in, com os números da lista e dividindo os valores por 2
impares = [numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]
outro_if = [numero if numero != 6 else 600 for numero in pares]


print(divisao)
print(impares)
print(pares)
print(outro_if)