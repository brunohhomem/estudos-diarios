"""""""""""""""
Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o 
Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua 
hora e a quantidade de horas trabalhadas no mês.
10% inss

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220
"""

valor_hora = float(input('Digite o valor de uma hora trabalhada: \n'))
horas = int(input('Digite a quantidade de horas trabalhadas: \n'))
salario_bruto = valor_hora * horas
salario_liquido = 0.0
desc_sindicato = 0.03
desc_inss = 0.1
pagto_fgts = 0.11

if 900 < salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    inss = salario_bruto * desc_inss
    sindicato = salario_bruto * desc_sindicato
    salario_liquido = salario_bruto - ir - inss - sindicato
    fgts = salario_bruto * pagto_fgts
elif 1500 < salario_bruto <= 2500:
    ir = salario_bruto * 0.1
    inss = salario_bruto * desc_inss
    sindicato = salario_bruto * desc_sindicato
    salario_liquido = salario_bruto - ir - inss - sindicato
    fgts = salario_bruto * pagto_fgts
elif salario_bruto > 2500:
    ir = salario_bruto * 0.2
    inss = salario_bruto * desc_inss
    sindicato = salario_bruto * desc_sindicato
    salario_liquido = salario_bruto - ir - inss - sindicato
    fgts = salario_bruto * pagto_fgts
else:
    ir = 0
    inss = salario_bruto * desc_inss
    sindicato = salario_bruto * desc_sindicato
    salario_liquido = salario_bruto - ir - inss - sindicato
    fgts = salario_bruto * pagto_fgts

print(f'Salário bruto: R${salario_bruto}')
print(f'FGTS: R${fgts}')
print(f'Imposto de renda: -R${ir}')
print(f'Sindicato: -R${sindicato}')
print(f'INSS: -R${inss}')


print(f'Salário liquido: R${salario_liquido}')
