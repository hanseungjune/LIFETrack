num = int(input('값을 입력해보시오 : '))
result = str(num)

if num >= 1000000000:
    result = str(num // 1000000000) + 'g'
elif num >= 1000000:
    result = str(num // 1000000) + 'M'
elif num >= 1000:
    result = str(num // 1000) + 'K'
else:
    pass

print(result)