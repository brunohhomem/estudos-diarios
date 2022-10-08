# Sistema de perguntas e respostas. Aula 63 — Curso de Python 3 — Luiz Miranda

print('Bem vindo ao teste de matemática.\nBoa sorte!')
print()

respostas_certas = 0
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '3', 'd': '5', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2 + 3?',
        'respostas': {'a': '1', 'b': '4', 'c': '3', 'd': '5', },
        'resposta_certa': 'd',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 2 - 1?',
        'respostas': {'a': '1', 'b': '4', 'c': '3', 'd': '5', },
        'resposta_certa': 'a',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 2 + 1?',
        'respostas': {'a': '1', 'b': '4', 'c': '3', 'd': '5', },
        'resposta_certa': 'c',
    },
}

# pk = Pergunta key // pv = Pergunta value
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Alternativas:')
    for rk, rv in pv['respostas'].items():  # rk = respostas key // rv = respostas value
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou! :D')
        respostas_certas += 1
    else:
        print('Você errou! :(')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {porcentagem_acerto}% das perguntas.')
