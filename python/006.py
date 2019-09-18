n = 100

sumSquared = (((n + 1) * n) // 2) ** 2

squaredSum = 0
for i in range(1, n + 1):
    squaredSum += i ** 2

result = sumSquared - squaredSum
print(result)