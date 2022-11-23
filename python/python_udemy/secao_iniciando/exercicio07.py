"""
Calculadora com While
"""

while True:
  n1 = input('Digite o primeiro número: ')
  n2 = input('Digite o segundo número: ')
  operador = input('Escolha a operação:\n[+]\n[-]\n[/]\n[*]\n')
  resultado = 0

  if operador == '+' or operador == '-' or operador == '/' or operador == '*':
    if n1.isdigit() and n2.isdigit():
      n1 = float(n1)
      n2 = float(n2)
      if operador == '+':
        resultado = n1 + n2
      elif operador == '-':
        resultado = n1 - n2      
      elif operador == '/':
        resultado = n1 / n2      
      elif operador == '*':
        resultado = n1 * n2    
    print(f'O resultado é: {resultado}')
  else:
    print('Você não digitou um número válido ou não selecionou uma operação válida.')

  sair = input('Quer [s]air? ').lower().startswith('s')
  if sair:
    break
