"""""""""""""""""""""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""

l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))

if l1 == l2 == l3:
    print('Temos um triângulo Equilátero, com 3 lados iguais.')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('Temos um triângulo Isósceles, com 2 lados iguais.')
else:
    print('Temos um triângulo Escaleno, com 3 lados diferentes.')
