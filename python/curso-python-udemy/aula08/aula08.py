""""""""""""""""""""""
- Criar variáveis para nome, idade, altura e peso de uma pessoa.
- Criar variável com ano atual
- Obter ano de nascimento da pessoa
- Obter o IMC da pessoa com 2 casas decimais
- Exibir um texto com todos os valores na tela usando F-strings(com as chaves)
"""
nome = 'Bruno'
idade = 28
altura = 1.67
peso = 84.500
ano_atual = 2022
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome}, nasceu em {ano_nasc} e completou {idade} anos em {ano_atual}.')
print(f'{nome}, pesa {peso} kilos, tem {altura} cm de altura e seu imc é de {imc:.2f}.')



