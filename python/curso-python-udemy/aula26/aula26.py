"""""""""
Desafio
for / while
"""

x = 0
y = 10

while x < 9 and y > 1:
    print(x, y)
    x += 1
    y -= 1
else:
    print(f'Terminei com while!')

print('-----------------------------------------------------------------------')

a = 0
b = 10

for numeros in range(0, 9, 1):
    print(a, b)
    a += 1
    b -= 1
else:
    print(f'Terminei com for!')
print('-----------------------------------------------------------------------')

#  Solução do instrutor

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
else:
    print(f'Solução do instrutor!')
    print('-----------------------------------------------------------------------')

