"""""""""""
Variáveis
    - Iniciar com letra, pode contar números, separar _, letras minúsculas.
"""
import datetime

nome = 'Bruno'
idade = 28
altura = 1.67
peso = 85
sexo = 'M'
today = datetime.date.today()
imc = peso/(altura**2)

print(nome, type(nome))
print(idade)
print(altura)
print(peso)
print(sexo)
print(idade > 18)
print(nome, 'tem', idade, 'de idade e seu imc é:', imc)

print(today)










