checknum = list(map(int, input().split()))[:5]

def checksum(checknum):
    sum = 0
    for i in checknum:
        sum += int(i) ** 2
    return sum % 10

print(checksum(checknum))
