import math

num = 600851475143

lastfactor = 1
while num % 2 == 0:
    lastFactor = 2
    num = num // 2

factor = 3
maxFactor = int(math.sqrt(num))
while num > 1 and factor <= maxFactor:
    while num % factor == 0:
        num = num // factor
        maxFactor = int(math.sqrt(num))
        lastFactor = factor
    factor += 2

if num == 1:
    print(lastFactor)
else:
    print(num)