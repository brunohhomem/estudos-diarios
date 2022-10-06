"""""""""""
 Validar CPF

 CPF = são 11 digitos (sem pontos e traço), os nove primeiros números são calculados com a formula abaixo para
 retirar o primeiro dígito verificador.
 O Segundo dígito verificador são calculados com os 10 primeiros números com a regra abaixo.

 Regras:      
 1° Dígito      2° Dígito  
 10 * 1         11 * 1
 9  * 2         10 * 2
 8  * 3         9  * 3
 7  * 4         8  * 4
 6  * 5         7  * 5
 5  * 6         6  * 6
 4  * 7         5  * 7
 3  * 8         4  * 8
 2  * 9         3  * 9
                2  * 10 
"""
from random import randint

numero = str(randint(100000000, 999999999))

novo_cpf = numero
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        novo_cpf += str(digito)

print(novo_cpf)
