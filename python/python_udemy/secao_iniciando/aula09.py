"""
Fatiamento de strings
Fatiamento [i:f:p] [::]
obs: A função len, retorna a quantidade de caracteres de uma str
Contagem de caracteres é diferente de índice (iniciando em 1)
"""

variavel = 'Olá mundo!'
print(variavel[0])
print(variavel[1])
print(variavel[2])
print(variavel[3])
print(variavel[4])
print(variavel[-5])
print(variavel[-4])
print(variavel[-3])
print(variavel[-2])

print(variavel[0:5])
print(variavel[::-1]) # Contando o passo com indice negativo, inverte a string
print(len(variavel))
