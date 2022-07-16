num = str(input())

def sumOfDigits(num):
    sum = 0
    for n in num:
        sum += int(n)
    return sum

print(sumOfDigits(num))