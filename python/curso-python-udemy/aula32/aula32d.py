nomes = ['bruno', 'vitória', 'butters', 'hermione']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes
]

print(novos_nomes)
