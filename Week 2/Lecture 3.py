from math import log

#function that checks if x is prime
def prime(x):
    for n in range(2, x):
        if x%n == 0:
            return False
    return True

#main function using ryan's algorithm
def challenge_solution_fast(n):
    x = 1
    for i in range(2,n):
        if prime(i):
            x *= i**int(log(n,i))
    return x
n = 50000
print(challenge_solution_fast(n))