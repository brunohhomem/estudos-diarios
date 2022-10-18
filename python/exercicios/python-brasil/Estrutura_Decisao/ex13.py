# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

dia = int(input('Digite o numero do dia da semana de 1 a 7: \n'))

if dia == 1:
    print(f'Dia {dia} = Domingo')
elif dia == 2:
    print(f'Dia {dia} = Segunda')
elif dia == 3:
    print(f'Dia {dia} = Terça')
elif dia == 4:
    print(f'Dia {dia} = Quarta')
elif dia == 5:
    print(f'Dia {dia} = Quinta')
elif dia == 6:
    print(f'Dia {dia} = Sexta')
elif dia == 7:
    print(f'Dia {dia} = Sábado')
else:
    print(f'Valor digitado:{dia} - inválido')
