#  Variavel em escopo global
variavel = 'valor'


def func():
    print(variavel)


def func2():
    #  Outra variável criada no escopo da função que só está acessivel a essa função
    variavel = 'outro valor'
    print(variavel)


func()
func2()

#  Print a variável global, a variavel global, não é alterada pela variavel local da func2
print(variavel)


def func3():
    global variavel
    variavel = 'Agora eu posso alterar o valor da variável.'
    print(variavel)


func3()
