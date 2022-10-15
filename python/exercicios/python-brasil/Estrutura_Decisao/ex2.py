# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input('Digite um valor: '))

if numero > 0:
    print(f'O número é positivo.')
elif numero == 0:
    print(f'O número é zero.')
else:
    print(f'O número é menor que zero, portanto, negativo.')
