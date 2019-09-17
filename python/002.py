max = 3999999

nMinus2 = 0
nMinus1 = 2
n = 4 * nMinus1 + nMinus2 # 8

sum = nMinus1

while n < max:
    sum += n

    nMinus2 = nMinus1 # 2
    nMinus1 = n # 8
    n = 4 * nMinus1 + nMinus2 # 34

print(sum)