import math 

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71] # len(primes) = 20
exps = [0 for x in range(len(primes))]
result = 1
i = 0
check = True
limit = math.sqrt(len(primes))

while primes[i] < len(primes):
    exps[i] = 1
    if check:
        if primes[i] <= limit:
            exps[i] = math.floor(math.log(len(primes), 10) / math.log(primes[i], 10))
        else:
            check = False
    result = result * primes[i] ** exps[i]
    i += 1
print(result)