# Desafio, fazer um pedra - papel - tesoura (Janken)
import random

print('Bem vindo ao pedra, papel e tesoura')

while True:
    escolha = input('Escolha: pedra, papel ou tesoura.\n')
    computador = random.randint(1, 3)
    escolha_comp = ''

    if computador == 1:
        escolha_comp = 'pedra'
    elif computador == 2:
        escolha_comp = 'papel'
    elif computador == 3:
        escolha_comp = 'tesoura'

    if escolha == escolha_comp:
        print(f'Empate! Ambos escolhemos {escolha}')
    else:
        if escolha == 'pedra' and escolha_comp == 'tesoura':
            print(f'Você escolheu: {escolha}, o computador escolheu: {escolha_comp}')
            print(f'Você venceu, {escolha} ganha de {escolha_comp}')
        elif escolha == 'papel' and escolha_comp == 'pedra':
            print(f'Você escolheu: {escolha}, o computador escolheu: {escolha_comp}')
            print(f'Você venceu, {escolha} ganha de {escolha_comp}')
        elif escolha == 'tesoura' and escolha_comp == 'papel':
            print(f'Você escolheu: {escolha}, o computador escolheu: {escolha_comp}')
            print(f'Você venceu, {escolha} ganha de {escolha_comp}')
        else:
            if escolha_comp == 'pedra' and escolha == 'tesoura':
                print(f'Você escolheu: {escolha}, o computador escolheu: {escolha_comp}')
                print(f'Você perdeu, {escolha_comp} ganha de {escolha}')
            elif escolha_comp == 'papel' and escolha == 'pedra':
                print(f'Você escolheu: {escolha}, o computador escolheu: {escolha_comp}')
                print(f'Você perdeu, {escolha_comp} ganha de {escolha}')
            elif escolha_comp == 'tesoura' and escolha == 'papel':
                print(f'Você escolheu: {escolha}, o computador escolheu: {escolha_comp}')
                print(f'Você perdeu, {escolha_comp} ganha de {escolha}')

    continua = input('Deseja continuar? s/n\n')

    if continua == 'n':
        break
