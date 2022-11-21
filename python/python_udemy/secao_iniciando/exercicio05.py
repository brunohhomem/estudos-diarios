"""
1 - Faça um programa que peça ao usuário para digitar um número inteiro, informe se esse número é
par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

2 - Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba
uma saudação apropriada. 
Ex. 0-11, bom dia, 12-17 boa tarde, 18-23 boa noite.

3 - Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva
"Seu nome é curto", entre 5-6 "Seu nome é normal", maior que 6 "seu nome é grande"
"""

#1

# numero = input('Digite um número: ')

# if numero.isdigit():
#   numero = int(numero)
#   if numero % 2 == 0:
#     print(f'Seu número {numero}, é par.')
#   else:
#     print(f'Seu número {numero}, é impar.')
# else:
#   print('Você não digitou um número inteiro.')

#2
# hora = input("Poderia me informar que horas são: ")

# if hora.isdigit():
#   hora = int(hora)
#   if hora >= 0 and hora < 6:
#     print('Boa madrugada!')
#   elif hora >= 6 and hora <= 11:
#     print('Bom dia!')
#   elif hora >= 12 and hora <= 17:
#     print('Boa Tarde!')
#   elif hora >= 18 and hora <= 23:
#     print('Boa noite!')
# else:
#   print('Você não informou uma hora válida, apenas números inteiros serão aceitos.')

# 3
nome = input('Por favor me informe seu nome? ')

if not nome.isdigit() :
  if len(nome) <= 4:
    print('Seu nome é muito curto.')
  elif len(nome) == 5 or len(nome) == 6: 
    print('Seu nome é normal.')
  elif len(nome) > 6:
    print('Seu nome é muito grande.')
else:
  print('Você não digitou um nome válido, por favor, digite apenas letras')

