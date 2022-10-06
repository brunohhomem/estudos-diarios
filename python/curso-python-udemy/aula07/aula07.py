nome = 'Bruno'
idade = 28
altura = 1.67
peso = 85
sexo = 'M'
imc = peso/(altura**2)

print(f'ashdajsdahsdahsdjhads')
print(nome, 'tem', idade, 'de idade e seu imc é:', imc)  # normal
print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')  # string formatada
print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome, idade, imc))  # Função .format

