def prime(n):
    L = list(range(2, n+1))
    L2 = L[:]

    for a in L:
        for b in L:
            if (b in L2) and ( a != b and b % a == 0 ):
                L2.remove(b)
    print(L2)

prime(int(input()))