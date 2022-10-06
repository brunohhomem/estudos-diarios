n1 = float(input('Digite a primeira nota: \n'))
n2 = float(input('Digite a segunda nota: \n'))
n3 = float(input('Digite a terceira nota: \n'))
n4 = float(input('Digite a quarta nota: \n'))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print('Parabéns você passou de ano.')
else:
    print('Sua média não foi suficiente para passar.')

print(f'Sua média é: {media}')