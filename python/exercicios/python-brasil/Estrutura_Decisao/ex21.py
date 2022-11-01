"""""""""""""""""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas 
existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, 
quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

print('Bem vinde ao banco.')
valor_saque = float(input('Qual o valor do saque?\n'))
lista_notas = [1, 5, 10, 50, 100]
valor_minimo = 10
valor_maximo = 600
unidade = 0
dezena = 0
centena = 0
saque = 0


if valor_minimo < valor_saque < valor_maximo:
    unidade = valor_saque % 10
    valor_saque = int(valor_saque - unidade) / 10
    dezena = valor_saque % 10
    dezena = int(dezena)
    valor_saque = (valor_saque - dezena) / 10
    centena = valor_saque % 10
    centena = int(centena)

    print(f'A centena{centena}')
    print(f'A dezena{dezena}')
    print(f'A centena{unidade}')