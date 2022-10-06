""""""""""
While em python
- Utilizado para realizar ações enquanto uma condição for verdadeira.
- continue
- break

Requisitos: Entender condições e operadores.
"""

x = 0

while x < 10:
    if x == 3:  # Nesse if, eu forço o x a receber o proximo acrescimo de valor sem ser apresentado em tela.
        x = x + 1
        continue  # continue força o código a pular as próximas instruções, mas como existe um loop, o código reinicia

    print(x)
    x = x + 1

print('Acabou o loop')

