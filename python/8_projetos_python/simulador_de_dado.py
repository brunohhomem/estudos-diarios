# Projeto 1 & 2
# Simular o uso de um dado, para gerar um valor de 1 a 6
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de jogar o dado?\n'
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('SIM'), sg.Button('NAO')]
        ]

    def Iniciar(self):
        # Janela
        self.janela = sg.Window('Simulador de Dados', layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # Fazer algo com os valores
        try:
            if self.eventos == 'SIM':
                self.GerarValorDoDado()
            elif self.eventos == 'NAO':
                print('Agradecemos sua participação.')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro com a sua resposta.')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
