"""""""""""""""""""""""""""
Entrada de dados
"""

""""""""""""""""""""""
nome = input('Qual seu nome? \n')
idade = input('Qual a sua idade? \n')

ano_nasc = 2022 - int(idade)
print(f'Seu nome é: {nome} e você tem {idade} anos de idade. Você nasceu em {ano_nasc}.')
"""""

# Calculadora
numero1 = input('Digite o primeiro número: \n')
numero2 = input('Digite o segundo número: \n')
numero3 = int(input('Digite o terceiro número: \n'))

print(f'O resultado é: {int(numero1)+int(numero2)}')
print(f'O terceiro número é {numero3} e o seu tipo de dado é {type(numero3)}')
