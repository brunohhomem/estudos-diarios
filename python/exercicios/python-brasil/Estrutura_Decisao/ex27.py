"""""""""""""""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de 
maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
fruta = int(input('Qual fruta deseja comprar? 1 - Morango | 2 - Maça\n'))
kilos = float(input('Quantos kilos?\n'))
valor_kilo = 0
total = 0

if fruta == 1 and kilos > 0:
    if kilos <= 5:
        valor_kilo = 2.50
    else:
        valor_kilo = 2.20

    total = kilos * valor_kilo
    if total > 25 or kilos > 8:
        total = total - (total * 0.1)

    print(f'O preço a pagar é: R${total:.2f}')
elif fruta == 2 and kilos > 0:
    if kilos <= 5:
        valor_kilo = 1.80
    else:
        valor_kilo = 1.50

    total = kilos * valor_kilo
    if total > 25 or kilos > 8:
        total = total - (total * 0.1)

    print(f'O preço a pagar é: R${total:.2f}')
else:
    print('Fruta ou quantidade indisponível.')
