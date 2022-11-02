""""""""""""""""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 
como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""
respostas = 0
print('***INVESTIGAÇÃO CRIMINAL***')
p1 = input('Telefonou para a vitima? (S/N)').upper()
respostas += 1 if p1 == 'S' else False
p2 = input('Esteve no local do crime? (S/N)').upper()
respostas += 1 if p2 == 'S' else False

p3 = input('Mora perto da vítima? (S/N)').upper()
respostas += 1 if p3 == 'S' else False

p4 = input('Devia para a vítima? (S/N)').upper()
respostas += 1 if p4 == 'S' else False

p5 = input('Já trabalhou com a vítima? (S/N)').upper()
respostas += 1 if p5 == 'S' else False

if respostas == 2:
    print('SUSPEITO')
elif 3 <= respostas <= 4:
    print('CÚMPLICE')
elif respostas == 5:
    print('ASSASSINO')
else:
    print('INOCENTE')
