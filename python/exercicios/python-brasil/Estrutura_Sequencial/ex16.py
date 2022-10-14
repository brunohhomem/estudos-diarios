""""""""""""""""""""""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a 
tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

tamanho_m2 = float(input('Por favor informe a quantidade de metros quadrados a serem pintados:\n'))
tinta = tamanho_m2 / 3
v_tinta = tinta * 80.0

print(f'Precisaremos de {tinta: .2f} latas de tinta. O valor final é de: R${v_tinta: .2f}')
