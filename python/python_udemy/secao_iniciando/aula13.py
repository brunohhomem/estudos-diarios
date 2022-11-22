"""
Repetições
while (enquanto)
Executa uma ação enquanto a condição for verdadeira
"""

condicao = True
x = 0

while condicao:
  print(x)
  x += 1
  if x == 50:
    break

# Sempre que o laço vê a palavra BREAK ele finaliza o loop
# Quando encontra a palavra continue, reseta o laço.