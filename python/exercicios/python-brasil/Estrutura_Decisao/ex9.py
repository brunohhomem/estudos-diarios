# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

lista.append(n1)
lista.append(n2)
lista.append(n3)

lista_ordenada = sorted(lista)
print(lista_ordenada)
