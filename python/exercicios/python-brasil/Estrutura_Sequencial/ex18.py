""""""""""""""""""""""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tam_arquivo = float(input('Digite o tamanho do arquivo em mb: '))
velocidade = float(input('Digite sua velocidade de download em mbps: '))

download = (tam_arquivo / velocidade) * 60

print(download)
