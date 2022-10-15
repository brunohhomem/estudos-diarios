"""""""""""""""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
sexo = input('Você é so sexo (m)asculino ou (f)eminino?')
altura = float(input('Digite sua altura em centimetros: '))
peso = 0

if sexo == 'm':
    peso = (72.7 * altura) - 58
elif sexo == 'f':
    peso = (62.1 * altura) - 44.7
else:
    print('Você precisa escolher entre (m)asculino ou (f)eminino.')

print(f'seu peso ideal é: {peso:.2f}')
