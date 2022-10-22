# Calculadora com funções
print('Calculadora em python:')
print('Adição +')
print('Subtração -')
print('Divisão /')
print('Multiplicação *')
print('Caso queira sair, digite a letra (s)air.')
print('')
executar = ''

while executar.upper() != 'S':
    executar = input('Deseja realizar uma operação matemática? (s)im:\n')


    def adiciona(a, b):
        return a + b


    def subtrai(a, b):
        return a - b


    def divide(a, b):
        return a / b


    def multiplica(a, b):
        return a * b


    if executar.upper() == 'S':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        operacao = input('Escolha qual operação deseja realizar: ')

        if operacao == '+':
            print(adiciona(n1, n2))
        elif operacao == '-':
            print(subtrai(n1, n2))
        elif operacao == '/':
            print(divide(n1, n2))
        elif operacao == '*':
            print(multiplica(n1, n2))
        else:
            print('Você não digitou uma operação válida')
            # print('O programa será encerrado')
            print('')
        executar = ''
    else:
        print('Você precisa digitar (s), caso queira fazer uma conta.')
