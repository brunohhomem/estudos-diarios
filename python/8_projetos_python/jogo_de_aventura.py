# Projeto 7 & 8 (GUI): Jogo de aventura;

# Eu quero chegar a finais diferentes na história, de acordo com as respostas para o programa.
# Qual o cenário? Uma guerra, entre duas nações. Temos dois lados, A e B. Somente Lado A vence.
# Devo tomar as decisões corretas para chegar a vitória
class JogoDeAventura():
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (norte/sul)\n'  # Norte A // Sul B
        self.pergunta2 = 'Você prefere espada ou escudo? (espada/escudo)\n'  # Espada A // Escudo B
        self.pergunta3 = 'Qual é a sua especialidade? (vanguarda/tatica)\n'  # Vanguarda A // Tático B
        self.finalHistoria1 = 'Você é o herói, vai liderar a vanguarda.'
        self.finalHistoria2 = 'Você é o herói. Proteja as nossas tropas.'
        self.finalHistoria3 = 'Você se sacrificou na batalha.'
        self.finalHistoria4 = 'Você não lutará nessa batalha.'

    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'norte':
            resposta2 = input(self.pergunta2)
            if resposta2 == 'espada':
                print(self.finalHistoria1)
            elif resposta2 == 'escudo':
                print(self.finalHistoria2)
        elif resposta1 == 'sul':
            resposta2 = input(self.pergunta3)
            if resposta2 == 'vanguarda':
                print(self.finalHistoria3)
            elif resposta2 == 'tatica':
                print(self.finalHistoria4)


jogo = JogoDeAventura()
jogo.Iniciar()
