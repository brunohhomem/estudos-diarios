"""""""""""""""""
1 - Crie uma função que exibe uma saudação com parametros, saudacao e nome.

2 - Crie uma função que recebe 3 numeros como parametros e exiba a soma entre eles

3 - Crie uma função que receba 2 numeros. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne
o valor do primeiro número somado ao aumento percentual do mesmo.

4 - Fizz Buzz - Se o parametro da função for divisivel por 3, retorne fizz, se o parametro da funcao for divisivel por 5
retorna buzz, se o parametro da função for divisivel  por 5 e por 3, retorne FizzBuzz, caso contrario, 
retorne o número errado.
"""

# def saudacao(sauda, nome):
#     print(sauda, nome)
#
#
# saudacao('oi', 'bruno')

# v1 = int(input('Digite o primeiro número: \n'))
# v2 = int(input('Digite o segundo número: \n'))
# v3 = int(input('Digite o terceiro número: \n'))
#
#
# def soma(n1, n2, n3):
#     return n1 + n2 + n3
#
#
# print(soma(v1, v2, v3))

# v1 = int(input('Digite o primeiro número: \n'))
# v2 = int(input('Digite o segundo número: \n'))
# v2 = v2/100
#
#
# def porcentagem(n1, n2):
#     return n1 + (n1 * n2)
#
#
# print(porcentagem(v1, v2))

def fb(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'fizzbuzz'
    elif numero % 5 == 0:
        return 'fizz'
    elif numero % 3 == 0:
        return 'buzz'
    return numero


from random import randint

for i in range(100):
   aleatorio = randint(0, 100)
   print(fb(aleatorio))


