def lista(numero):
    return list(str(numero) * numero)

numero = int(input('Digite o número: '))

for linha in range(1, numero + 1):
    print(' '.join(lista(linha)))
