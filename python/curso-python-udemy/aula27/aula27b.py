"""""""""""""""""""""
 - Funções def em python - *args **kwargs
"""


def func(*args, **kwargs):
    print(args)
    print(len(args))

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)


func('123', 2, 3, 4, nome='bruno', idade=28)
