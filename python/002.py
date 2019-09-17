max = 3999999

nMinus2 = 1
nMinus1 = 2
n = nMinus1 + nMinus2 # 3

sum = 0

while nMinus1 < max:
    sum += nMinus1

    nMinus2 = nMinus1 + n # 5
    nMinus1 = n + nMinus2 # 8
    n = nMinus1 + nMinus2 # 13

print(sum)