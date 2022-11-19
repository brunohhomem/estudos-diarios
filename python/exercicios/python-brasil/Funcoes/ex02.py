n = int(input('Digite o número: '))

def lista(n):
    for i in range(1, n + 1):
        l = []
        for j in range(i):
            l.append(str(j+1))
        print(' '.join(l))
lista(n)