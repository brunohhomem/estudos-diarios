""" Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""

# nome = 'bruno'
# preco = 1000.95887744
# variavel = '%s, o preço total foi R$%.2f:.' % (nome, preco)
# print(variavel)
# print('o hexadecimal de %d é %08X' % (15, 15))

"""
Formatação básica de strings
s - strings
d - int
f - float

.<numero de dígitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
sinal + ou -
ex: 0 > - 100, .1f
conversion flags - !r, !s, !s
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.45464654:.1f}')
