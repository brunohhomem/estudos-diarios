"""""""""""""""""""""""
1 - Faça um programa que peça ao usuário para digitar um número inteiro, informe se esse número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.

2 - Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex. Bom dia 0-11; Boa tarde 12-17, Boa noite 18-23.

hora = input('Digite a hora: ')
hora = int(hora)

if hora >= 0 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
else:
    print('Boa noite')

3 - Faça um programa que peça o primeiro nome de usuário. Se o nome tiver 4 letras ou menos escreva: "O nome é curto";
se tiver entre 5 e 6 letras, escreva: "Seu nome é normal"; maior que 6 escreva: "Seu nome é muito grande".

nome = input('Digite seu nome por favor: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print("O nome é curto")
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')
elif tamanho_nome > 6:
    print('Seu nome é muito grande.')

"""""""""

n1 = input('Digite um número: ')
if n1.isnumeric():
    n1 = int(n1)
    dividir = n1 % 2
    print(dividir)
    if dividir == 1:
        print('Seu número é ímpar.')
    else:
        print('Seu número é par.')
else:
    print('Você não digitou um número inteiro válido. Por favor, digite um número inteiro para continuar.')











