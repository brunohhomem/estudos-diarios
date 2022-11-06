# Multi janelas
import PySimpleGUI as sg


# Criar layout e aplicar estilo
def janela_login():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Nome')],
        [sg.Input('')],
        [sg.Button('Continuar')]
    ]

    return sg.Window('Login', layout, finalize=True)


def janela_pedido():
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Fazer pedido')],
        [sg.Checkbox('Pizza Pepperoni', key='pizza1'), sg.Checkbox('Pizza de Frango com Catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
    ]
    return sg.Window('Montar Pedido', layout, finalize=True)


# Criar janelas iniciais
janela1, janela2, = janela_login(), None
# Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada:
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para a próxima janela:
    if window == janela1 and event == 'Continuar':
        janela1.hide()
        janela2 = janela_pedido()
    # Quando queremos voltar para a janela anterior:
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] and values['pizza2']:
            sg.popup('Foi solicitado uma pizza de pepperoni e uma pizza de frango com catupiry.')
        elif values['pizza1']:
            sg.popup('Foi solicitado uma pizza de pepperoni.')
        elif values['pizza2']:
            sg.popup('Foi solicitado uma pizza de frango com catupiry.')
        else:
            sg.popup('Nenhuma pizza selecionada.')
# Lógica dos eventos
