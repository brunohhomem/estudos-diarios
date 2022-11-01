# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.

numero = float(input('Digite um número:\n'))

if numero == round(numero):
    print('inteiro')
else:
    print('decimal')
    print("Arredondado pra baixo: ", round(numero - 0.5))
    print("Arredondado pra cima : ", round(numero + 0.5))