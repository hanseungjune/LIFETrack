while True:
    numbers = list(map(int, input().split()))[:3]
    if sum(numbers) == 0:
        break
    max_nums = max(numbers)
    numbers.remove(max_nums)
    if numbers[0]**2 + numbers[1]**2 == max_nums**2:
        print("right")
    else:
        print("wrong")