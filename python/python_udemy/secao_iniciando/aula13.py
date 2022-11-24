"""
Repetições
while (enquanto)
Executa uma ação enquanto a condição for verdadeira
"""

# Sempre que o laço vê a palavra BREAK ele finaliza o loop
# Quando encontra a palavra continue, reseta o laço.

# condicao = True
# x = 0

# while condicao:
#   print(x)
#   x += 1
#   if x == 50:
#     break

# qtd_linha = 5
# qtd_colunas = 5
# linha = 1
# coluna = 0

# # Laços internos While dentro de While
# while linha <= qtd_linha:
#   coluna = 1

#   while coluna <= qtd_colunas:
#     print(f'Linha: {linha}, Coluna: {coluna}')
#     coluna += 1
#   linha += 1

# print('Acabou')

string = 'Qualquer valor'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('Else do while')
