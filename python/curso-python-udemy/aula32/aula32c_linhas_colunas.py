# Linhas e colunas

# for x in range(1, 11):
#     for y in range(1, 6):
#         print(x, y)

linhas_e_colunas = [
    (a, b)
    if b != 2 else (a, b * 1000)
    for a in range(1, 11)
    for b in range(1, 6)
    if a != 3
]

print(linhas_e_colunas)