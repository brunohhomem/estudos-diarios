secreto = 'perfume'
digitada = []
chances = 3

while True:
    if chances == 0:
        print('VOCÊ PERDEU!')
        break

    letra = input('Digite uma letra: \n')

    if len(letra) > 1:
        print('Só vale uma letra por vez.')
        continue

    digitada.append(letra)

    if letra in secreto:
        print(f'Você descobriu uma letra. a letra "{letra.upper()}", existe na nossa palavra secreta.')
    else:
        print(f'Infelizmente a letra "{letra.upper()}", não faz parte da palavra secreta')
        digitada.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitada:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    print(secreto_temp)
    if secreto_temp == secreto:
        print(f'Parabéns vc ganhou. A palavra secreta é: {secreto_temp.upper()}')
        break
    else:
        print(f'Você ainda não descobriu a palavra secreta. Você acertou essas letras: {secreto_temp.upper()}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances')
