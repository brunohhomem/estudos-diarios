s1 = {0,1,2,3,4,5}
s2 = {1,2,3,4,5,6}

s3 = s1 | s2
print(f'Unindo dois sets:\n{s3}')
print()
s3 = s1 & s2
print(f'Mostrando valores presentes nos 2 sets:\n{s3}')
print()
s3 = s1 - s2
print(f'Pegando apenas os elementos no set da esquerda:\n{s3}')
print()
s3 = s1 ^ s2
print(f'Elementos únicos entre cada set:\n{s3}')