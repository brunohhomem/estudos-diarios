"""""""""""""""""""""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

- par ou ímpar;
- positivo ou negativo;
- inteiro ou decimal.
"""

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
operacao = int(input('Qual operação deseja realizar? \n1 - ADICIONA\n2 - SUBTRAI\n3 - DIVIDE\n4 - MULTIPLICA\n'))
resultado = 0.0


def adiciona(a, b):
    return a + b


def subtrai(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiplica(a, b):
    return a * b


def classifica_resultado(r):
    if r % 2 == 0:
        print(f'{r} é par.')
    else:
        print(f'{r} é ímpar.')

    if r == 0:
        print(f'{r} é um número neutro.')
    elif r > 0:
        print(f'{r} é positivo.')
    else:
        print(f'{r} é negativo.')

    if r == round(r):
        print(f'{r} é inteiro.')
    else:
        print(f'{r} é decimal.')


if operacao == 1:
    resultado = adiciona(a, b)
    print(f'O resultado da soma é: {resultado}')
    classifica_resultado(resultado)
elif operacao == 2:
    resultado = subtrai(a, b)
    print(f'O resultado da subtração é: {resultado}')
    classifica_resultado(resultado)
elif operacao == 3:
    resultado = divide(a, b)
    print(f'O resultado da divisão é: {resultado}')
    classifica_resultado(resultado)
elif operacao == 4:
    resultado = multiplica(a, b)
    print(f'O resultado da multiplicação é: {resultado}')
    classifica_resultado(resultado)
else:
    print('Você não selecionou uma operação válida.')
