"""""""""""
 - Índices
 - 0123456789.............................33
"""

frase = 'o rato roeu a roupa do rei de roma'
tam_frase = len(frase)
contador = 0
nova_string = ''

letra_do_usuario = input('Qual a letra deseja colocar maiúscula: \n')

# Iteração - Percorrer cada um dos elementos do seu objeto iterável.
while contador < tam_frase:
    letra = frase[contador]
    if letra == letra_do_usuario:
        nova_string += letra_do_usuario.upper()
    else:
        nova_string += letra

    print(nova_string)
    contador += 1


