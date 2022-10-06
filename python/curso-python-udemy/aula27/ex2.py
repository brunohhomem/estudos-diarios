"""""""""""""""""
1 - Crie uma função 1 que recebe uma função 2 como parâmetro e retorne o valor da função 2 executada.

2 - Crie uma função 1 que recebe uma função 2 como parâmetro e retorne o valor da função 2 executada. 
Faça a função 1 executar duas funções que recebem um número diferente de argumentos.
"""


# def ola_mundo():
#     return 'olá mundo!'
#
#
# def mestre(funcao):
#     return funcao()
#
#
# executando = mestre(ola_mundo)
#
# print(executando)

# def master():
#     slave()
#
#
# def slave():
#     return 5 + 5
#
#
# print(master())

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'oi {nome}'


def saudacao(nome, cumprimento):
    return f'{cumprimento} {nome}'


executando = mestre(fala_oi, 'Bruno')
executando2 = mestre(saudacao, 'Bruno', cumprimento='bom dia!')

print(executando)
print(executando2)