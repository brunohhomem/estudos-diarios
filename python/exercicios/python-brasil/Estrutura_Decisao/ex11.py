"""""""""""""""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
baseado no salário atual:

- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
"""

salario = float(input('Digite o salário: '))


def aumento(var1):
    novo_salario = 0.0
    percentual = 0
    resultado = ()

    if salario <= 280:
        percentual = 0.2
        novo_salario = salario + (salario * percentual)
        resultado = (
            percentual, novo_salario
        )
        return resultado
    elif 280 < salario <= 700:
        percentual = 0.15
        novo_salario = salario + (salario * percentual)
        return novo_salario
    elif 700 < salario <= 1500:
        percentual = 0.1
        novo_salario = salario + (salario * percentual)
        return novo_salario
    elif salario > 1500:
        percentual = 0.5
        novo_salario = salario + (salario * percentual)
        return novo_salario, percentual


print(aumento(salario))
