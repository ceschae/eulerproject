max = 1000
sum = 0

for x in range(1, max):
    if x % 3 == 0 or x % 5 == 0:
        sum += x

print(sum)