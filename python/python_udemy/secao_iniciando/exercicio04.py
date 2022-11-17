"""
Peça ao usuário para digitar o nome
Peça ao usuário para digitar sua idade

Se o nome e a idade forem digitados:
  Exiba:
    Seu nome é:
    Seu nome invertido é:
    Seu nome contem (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é {letra}
Se nada for digitado:
  Exiba:
    Você deixou os campos vazios.
"""

nome = input('Por favor, digite seu nome: ')
idade = input('Por favor, digite sua idade: ')
tamanho_nome = len(nome)

if nome and idade.isdigit():
  idade = int(idade)

  print(f'Seu nome é: {nome}')
  print(f'Seu nome invertido é: {nome[::-1]}')
  if ' ' in nome:
    print(f'Seu nome contém espaços.')
  else:
    print('Seu nome não contém espaços.')
  print(f'Seu nome tem {tamanho_nome} letras')
  print(f'A primeira letra do seu nome é: {nome[0]}')
  print(f'A ultima letra do seu nome é: {nome[(tamanho_nome - 1)]}')
  print(f'A ultima letra do seu nome é: {nome[-1]}')
else:
  print('Você deixou os campos vazios.')