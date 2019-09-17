max = 999

def SumOfMultiplesOf(n):
    nearestInt = max // n
    return n * (nearestInt * (nearestInt + 1)) // 2

result = SumOfMultiplesOf(3) + SumOfMultiplesOf(5) - SumOfMultiplesOf(15)

print(result)