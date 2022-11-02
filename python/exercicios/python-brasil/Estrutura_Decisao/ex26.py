""""""""""""""""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago 
pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

"""

preco_alcool = 1.90
preco_gasolina = 2.50
desc_min_gas = 0.04
desc_max_gas = 0.06
desc_min_alc = 0.03
desc_max_alc = 0.05
valor = 0
calc_desconto = 0
valor_final = 0

produto = input('Deseja abastecer? A-Álcool ou G-Gasolina?\n').upper()
litros = int(input('Quantos litros?\n'))

if produto == 'A':
    print(f'O pedido é {litros} litros de Álcool. O valor é de R${preco_alcool} por litro.')
    if litros <= 20:
        valor = litros * preco_alcool
        calc_desconto = valor * (desc_min_alc * litros)
        valor_final = valor - calc_desconto
        print(f'Valor total: R${valor}')
        print(f'Você terá um desconto de R${calc_desconto}. O valor final a pagar é: R${valor_final} ')
    elif litros > 20:
        valor = litros * preco_alcool
        calc_desconto = valor * (desc_max_alc * litros)
        valor_final = valor - calc_desconto
        print(f'Valor total: R${valor}')
        print(f'Você terá um desconto de R${calc_desconto}. O valor final a pagar é: R${valor_final} ')
    else:
        print('Quantidade inválida.')
elif produto == 'G':
    print(f'O pedido é {litros} litros de Gasolina. O valor é de R${preco_gasolina} por litro.')
    if litros <= 20:
        valor = litros * preco_gasolina
        calc_desconto = valor * (desc_min_gas * litros)
        valor_final = valor - calc_desconto
        print(f'Valor total: R${valor}')
        print(f'Você terá um desconto de R${calc_desconto}. O valor final a pagar é: R${valor_final} ')
    elif litros > 20:
        valor = litros * preco_gasolina
        calc_desconto = valor * (desc_max_gas * litros)
        valor_final = valor - calc_desconto
        print(f'Valor total: R${valor}')
        print(f'Você terá um desconto de R${calc_desconto}. O valor final a pagar é: R${valor_final} ')
    else:
        print('Quantidade inválida.')
else:
    print('Você não escolheu um produto válido.')
