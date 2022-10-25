"""""""""""""""""""""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numero = int(input('Digite um número inteiro menor que 1000:\n'))

unidade = numero % 10
numero = (numero - unidade) / 10
dezena = numero % 10
dezena = int(dezena)
numero = (numero - dezena) / 10
centena = numero % 10
centena = int(centena)

if unidade > 1:
    print(f'{unidade} unidades')
else:
    print(f'{unidade} unidade')

if dezena > 1:
    print(f'{dezena} dezenas')
else:
    print(f'{dezena} dezena')

if centena > 1:
    print(f'{centena} centenas')
else:
    print(f'{centena} centena')


