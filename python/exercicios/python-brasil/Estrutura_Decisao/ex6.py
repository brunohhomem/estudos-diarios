# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('digite 1° número: '))
n2 = int(input('digite 2° número: '))
n3 = int(input('digite 3° número: '))

if n1 > n2 and n1 > n3:
    print('primeiro é maior')
elif n2 > n1 and n2 > n3:
    print('Segundo número é maior.')
elif n3 > n1 and n3 > n2:
    print('O terceiro é maior')
else:
    print('Todos os números são iguais')
