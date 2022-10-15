# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

n1 = float(input('Qual o valor do primeiro produto: '))
n2 = float(input('Qual o valor do segundo produto: '))
n3 = float(input('Qual o valor do terceiro produto: '))

if n1 < n2 and n1 < n3:
    print('o primeiro é mais barato')
elif n2 < n1 and n2 < n3:
    print('o segundo é mais barato')
elif n3 < n1 and n3 < n2:
    print('o terceiro é mais barato')
else:
    print('todos são o mesmo valor')
