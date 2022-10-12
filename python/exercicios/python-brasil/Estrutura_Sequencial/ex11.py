# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com metade do segundo.
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.

n1 = int(input('Digite um número inteiro:\n'))
n2 = int(input('Digite outro número inteiro:\n'))
n3 = float(input('Digite um número real:\n'))

r1 = (n1 * 2) + (n2 / 2)
r2 = (n1 * 3) + n3
r3 = n3 * n3 * n3

print(f'o produto do dobro do primeiro com metade do segundo: {r1}')
print(f'a soma do triplo do primeiro com o terceiro: {r2}')
print(f'o terceiro elevado ao cubo {r3}')
