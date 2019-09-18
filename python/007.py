primes = []
goal = 10001

def isPrime(n):
    for i in range(1, len(primes)): # we don't have to check 2 if we're always sending odd numbers
        if n % primes[i] == 0:
            return False
    return True

primes.append(2)
n = 3
while len(primes) < goal:
    if isPrime(n):
        primes.append(n)
    n += 2

print(primes[goal - 1])