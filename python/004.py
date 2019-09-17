max = 0

def isPalindrome(n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n = n // 10
    for i in range(0, len(digits)):
        if digits[i] != digits[len(digits) - 1 - i]:
            return False
    return True

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        num = i * j
        if isPalindrome(num):
            if num > max:
                max = num
                print(max)
            break