# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O primeiro número é maior.')
elif n2 > n1:
    print(f'O segundo número é maior.')
elif n1 == n2:
    print(f'Os dois números são iguais.')