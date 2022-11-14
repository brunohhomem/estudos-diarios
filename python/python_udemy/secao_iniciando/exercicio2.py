# Calcular IMG

nome = input('Qual seu nome?\n')
altura = float(input('Qual sua altura?\n'))
peso = float(input('Qual seu peso?\n'))

imc = peso / (altura * altura)

print(f'{nome}, tem {altura} centímetros de altura. Pesa {peso}kgs')
print(f'{nome}, tem {imc:.2f}kg/m² de imc calculado.')
print()
