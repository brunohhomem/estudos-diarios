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

# print('Bem vinde ao banco.')
# numero = int(input('Valor para sacar (10-600):\n'))
# cem = int(numero / 100)
# numero = numero - (cem * 100)
#
# cinquenta = int(numero / 50)
# numero = numero - (cinquenta*50)
#
# dez = int(numero / 10)
# numero = numero - (dez * 10)
#
# cinco = int(numero / 5)
# numero = numero - (cinco * 5)
#
# um = numero
#
# print('Notas R$100,00 = ', cem)
# print('Notas R$50,00 = ', cinquenta)
# print('Notas R$10,00 = ', dez)
# print('Notas R$5,00 = ', cinco)
# print('Notas R$1,00 = ', um)


print("Valor mínimo do saque: R$10,00.")
print("Valor máximo do saque: R$600,00")
saque = int(input("Valor do saque: R$"))

while (saque < 10) or (saque > 600):
    print("Valor fora dos limites.")
    saque = int(input("Digite novamente: R$"))

if (saque >= 10) and (saque <= 600):
    resto1 = saque % 100
    resto2 = resto1 % 50
    resto3 = resto2 % 10
    resto4 = resto3 % 5
    nota100, nota50, nota10, nota5, nota1 = saque // 100, resto1 // 50, resto2 // 10, resto3 // 5, resto4 // 1
    print("R$100,00:", nota100)
    print("R50,00:", nota50)
    print("R$10,00:", nota10)
    print("R$5,00:", nota5)
    print("R$1,00:", nota1)
