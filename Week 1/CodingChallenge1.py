#checks if x is prime
def prime(x):
    for n in range(2, x):
        if x%n == 0:
            return False
    return True

#main function
def LCM(n):
    if (n==1):
        return n

    #sort out nonfactors and primes
    nonfactors = []
    primes = []
    for i in range(2, n):
        if (n%i != 0):
            nonfactors.append(i)
        if prime(i):
            primes.append(i)

    #since 'nonfactors' is the list we check if it's a factor,
    #we must account for 'n' as well as nonfactors, so we append this to the end
    nonfactors.append(n)

    #minimum incrementing factor is the product of all primes
    minimum = 1
    for i in range(1, len(primes)):
        minimum*=primes[i]

    scalingFactor = 1
    if n >= 25:
        scalingFactor = 200
    if n >= 15:
        scalingFactor = 20


    #time to do the bruteforcing! now with a massive incrementing value though!
    bool = True
    x = minimum*scalingFactor
    while bool:
        x+=minimum
        for i in range(len(nonfactors)):
            if (x%nonfactors[i] != 0):
                break
            if (i == len(nonfactors)-1 and bool):
                bool = False
    return x

for i in range(1, 30):
    print(LCM(i))
