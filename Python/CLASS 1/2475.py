checknum = list(map(int, input().split()))[:5]

sum = 0
for i in checknum:
    sum += int(i) ** 2

print(sum%10)
