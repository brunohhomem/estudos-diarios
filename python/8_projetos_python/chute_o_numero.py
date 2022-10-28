# Projeto 3 & 4
# Chutar um número que o algoritmo escolheu até acertar.
import random


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()

        try:
            while self.tentar_novamente:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print(f'Chute um valor mais baixo.\n{"*" * 20}')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print(f'Chute um valor mais alto.\n{"*" * 20}')
                    self.PedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print(f'Parabéns você acertou o número {self.valor_aleatorio}')
        except:
            print('Favor digitar apenas números.')

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número de 1 a 100:\n')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()