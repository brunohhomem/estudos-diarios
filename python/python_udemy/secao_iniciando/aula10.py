"""
Introdução ao try/except
  try > tentar executar o código
  except > ocorreu algum erro ao tentar executar  
"""

numero = input('Vou dobrar o numero que você digitar: ')

try:
  print('STR', numero)
  numero_float = float(numero)
  print('Float', numero_float)
  print(f'O dobro de {numero} é {numero_float}')
except:
  print('isso não é um número.')