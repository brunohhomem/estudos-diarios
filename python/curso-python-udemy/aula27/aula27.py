"""""""""""""""
Funções - def em Python
"""


# def saudacao(msg='Olá', nome='Usuário'):
#     print(msg, nome)
#
#
# saudacao('Bem vindo')
# saudacao(nome='Bruno')

v1 = input('Valor 1: \n')
v1 = int(v1)
v2 = input('Valor 2: \n')
v2 = int(v2)


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


resultado = divisao(v1, v2)

if resultado:
    print(resultado)
else:
    print('Conta inválida')
