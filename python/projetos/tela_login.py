# Sistema de login com PySimpleGUI
import PySimpleGUI as sg  # Importando o PySimpleGUI

# layout é baseado em linhas (cada lista) e colunas.
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'bruno' and valores['senha'] == '123':
            print('Bem vindo')
        else:
            print('Informações de login incorretas.')
