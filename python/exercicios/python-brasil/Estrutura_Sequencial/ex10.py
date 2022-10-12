# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = input('Digite a temperatura em graus celsius:\n')
celsius = float(celsius)
fahrenheit = (celsius * 1.8) + 32

print(f'{fahrenheit:.2f}')