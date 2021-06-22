def makePrime(n):
    lista=[i for i in range(2,n+1)]
    for i, k in enumerate(lista):
        if i<=int(n**.5):
            for j in lista[i+1:]:
                if j % k == 0:
                    lista.remove(j)
    return lista