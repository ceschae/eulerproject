num = 600851475143

def isPrime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    print(n, end=", ")
    return True

for x in range(num // 2, 1, -1):
    if num % x == 0 and isPrime(x):
        print(x)
        break