# Verificar qual número é maior.

n1 = input('Digite um número: ')

if n1.isdigit():
  n1_inteiro = int(n1)
  
  n2 = input('Digite outro número: ')
  
  if n2.isdigit():
    n2_inteiro = int(n2)
  else:
    print('Somente números inteiros são aceitos.')

else:
    print('Somente números inteiros são aceitos.')

if n1_inteiro > n2_inteiro:
  print(f'O primeiro número ({n1_inteiro}), é maior que o segundo número ({n2_inteiro})')
elif n2_inteiro > n1_inteiro:
  print(f'O primeiro número ({n1_inteiro}), é menor que o segundo número ({n2_inteiro})')
else:
  print('Ambos os números são iguais.')

print('\nFim\n')
