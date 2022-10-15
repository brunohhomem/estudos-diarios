# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('digite 1° número: '))
n2 = int(input('digite 2° número: '))
n3 = int(input('digite 3° número: '))

if n1 > n2 and n1 > n3:
    print('primeiro é maior')
    if n2 > n3:
        print('o terceiro é o menor')
    elif n3 > n2:
        print('O segundo é menor')
    else:
        print('os outros dois numeros são iguais')
elif n2 > n1 and n2 > n3:
    print('Segundo número é maior.')
    if n1 > n3:
        print('o primeiro é o menor')
    elif n3 > n1:
        print('O segundo é menor')
    else:
        print('os outros dois numeros são iguais')
elif n3 > n1 and n3 > n2:
    print('O terceiro é maior')
    if n1 > n2:
        print('o segundo é o menor')
    elif n2 > n1:
        print('O primeiro é menor')
    else:
        print('os outros dois numeros são iguais')
else:
    print('Todos os números são iguais')
