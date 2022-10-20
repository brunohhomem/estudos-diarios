""""""""""""""""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e 
calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0          A
  Entre 7.5 e 9.0           B
  Entre 6.0 e 7.5           C
  Entre 4.0 e 6.0           D
  Entre 4.0 e zero          E
  
  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito 
  for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2


if 9 <= media <= 10:
    print(f'A sua primeira nota foi: {n1}')
    print(f'A sua segunda nota foi: {n2}')
    print(f'A sua média foi: {media}')
    print('Seu conceito final é A. Você foi Aprovado.')
elif 7.5 <= media < 9:
    print(f'A sua primeira nota foi: {n1}')
    print(f'A sua segunda nota foi: {n2}')
    print(f'A sua média foi: {media}')
    print('Seu conceito final é B. Você foi Aprovado.')
elif 6 <= media < 7.5:
    print(f'A sua primeira nota foi: {n1}')
    print(f'A sua segunda nota foi: {n2}')
    print(f'A sua média foi: {media}')
    print('Seu conceito final é C. Você foi Aprovado.')
elif 4 <= media < 6:
    print(f'A sua primeira nota foi: {n1}')
    print(f'A sua segunda nota foi: {n2}')
    print(f'A sua média foi: {media}')
    print('Seu conceito final é D. Você foi REPROVADO.')
elif 4 < media >= 0:
    print(f'A sua primeira nota foi: {n1}')
    print(f'A sua segunda nota foi: {n2}')
    print(f'A sua média foi: {media}')
    print('Seu conceito final é E. Você foi REPROVADO.')
else:
    print('Você digitou valores válidos?')


