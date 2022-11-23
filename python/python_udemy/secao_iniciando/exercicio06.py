"""
Iterando strings com while
"""

nome = 'Bruno Henrique'  # iterável
nova_string = ''

index = 0
while index < len(nome):
  nova_string += nome[index] + '*'
  index += 1
print(nova_string)