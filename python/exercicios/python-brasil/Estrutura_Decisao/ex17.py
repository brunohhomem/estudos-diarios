# Faça um Programa que peça um número correspondente a um determinado
# ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Digite um ano para saber se ele é bissexto: '))

bissexto = ano % 4 == 0

print(bissexto)