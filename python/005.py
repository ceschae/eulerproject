import sys

def divAll(n):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True

num = 20
for num in range(20, sys.maxsize, 20):
    if divAll(num):
        print(num)
        break
    else:
        num += 1