# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra:\n')

if letra.upper() == 'A' or letra.upper() == 'E' or letra.upper() == 'I' or letra.upper() == 'O' or letra.upper() == 'U':
    print('Sua letra é uma vogal.')
else:
    print('Sua letra é uma consoante.')
