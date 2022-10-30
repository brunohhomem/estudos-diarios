# Projeto 7 & 8 (GUI): Jogo de aventura;
import PySimpleGUI as sg


# Eu quero chegar a finais diferentes na história, de acordo com as respostas para o programa.
# Qual o cenário? Uma guerra, entre duas nações. Temos dois lados, A e B. Somente Lado A vence.
# Devo tomar as decisões corretas para chegar a vitória
class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (norte/sul)\n'  # Norte A // Sul B
        self.pergunta2 = 'Você prefere espada ou escudo? (espada/escudo)\n'  # Espada A // Escudo B
        self.pergunta3 = 'Qual é a sua especialidade? (vanguarda/tatica)\n'  # Vanguarda A // Tático B
        self.finalHistoria1 = 'Você é o herói, vai liderar a vanguarda.'
        self.finalHistoria2 = 'Você é o herói. Proteja as nossas tropas.'
        self.finalHistoria3 = 'Você se sacrificou na batalha.'
        self.finalHistoria4 = 'Você não lutará nessa batalha.'

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Output(size=(30, 0), key='respostas')],
            [sg.Input(size=(25, 0), key='escolha')],
            [sg.Button('Responder')],
        ]
        # Criar Janela
        self.janela = sg.Window('Jogo de aventura!',layout=layout)
        # Ler os dados
        self.LerValores()
        # Fazer algo com os dados
        print(self.pergunta1)
        self.LerValores()
        if self.valores['escolha'] == 'n':
            print(self.pergunta2)
            self.LerValores()
            if self.valores['escolha'] == 'espada':
                print(self.finalHistoria1)
            elif self.valores['escolha'] == 'escudo':
                print(self.finalHistoria2)
        elif self.valores['escolha'] == 'sul':
            print(self.pergunta3)
            self.LerValores()
            if self.valores['escolha'] == 'vanguarda':
                print(self.finalHistoria3)
            elif self.valores['escolha'] == 'tatica':
                print(self.finalHistoria4)


    def LerValores(self):
        self.evento, self.valores = self.janela.Read()


jogo = JogoDeAventura()
jogo.Iniciar()
