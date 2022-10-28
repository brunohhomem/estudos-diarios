# Projeto 3 & 4
# Chutar um número que o algoritmo escolheu até acertar.
import random
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute', size=(30, 0))],
            [sg.Input(size=(25, 0), key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(30, 20))]
        ]
        # Janela
        self.janela = sg.Window('CHUTE O NÚMERO!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber os valores
                self.evento, self.valores = self.janela.Read()
                # Fazer algo com os valores
                if self.evento == 'Chutar':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print(f'Seu chute foi: {self.valor_do_chute}. Chute um valor mais baixo.\n{"*" * 20}')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print(f'Seu chute foi: {self.valor_do_chute}. Chute um valor mais alto.\n{"*" * 20}')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print(f'Parabéns você acertou o número {self.valor_aleatorio}')
                            break
        except:
            print('Favor digitar apenas números.')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()
