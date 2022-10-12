# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fahrenheit = input('Digite a temperatura em graus fahrenheit:\n')
fahrenheit = float(fahrenheit)
celsius = 5 * ((fahrenheit - 32) / 9)

print(f'{celsius:.2f}')
