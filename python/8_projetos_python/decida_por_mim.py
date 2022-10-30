# - Projeto 5 & 6(GUI): Decida por mim;
import random
import PySimpleGUI as sg


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei. Você quem sabe.',
            'Não faça isso.',
            'Acho que está na hora certa!'
        ]

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(45, 10))],
            [sg.Button('Decida por mim')]
        ]
        # Criar Janela
        self.janela = sg.Window('Decida por mim', layout=layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()
