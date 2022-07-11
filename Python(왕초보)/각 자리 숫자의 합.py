def sumOfDigits(num):
    digits = map(int, list(str(num)))
    return sum(digits)

print(sumOfDigits(47523))