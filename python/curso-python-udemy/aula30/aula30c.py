d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
v = d1

v[1] = 'Bruno'

print(d1)
print(v)

d1.pop(3)
print(d1)

d2 = {'a': 1, 'b': 2}
print(d2)

d1.update(d2)  # Junção dos valores do d1 com d2
print(d1)
