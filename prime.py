def isPrime(x): #x>2
    for i in range(2, int(x ** 0.5 + 1)): #+1, da param 2 excl.
        if x % i == 0:
            return False
    return True

#gibt alle Primzahlen zwischen 1 und 100 aus
print([ x for x in range(1, 100) if isPrime(x) ])
