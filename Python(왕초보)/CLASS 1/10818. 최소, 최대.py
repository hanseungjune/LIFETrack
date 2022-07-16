T = int(input())

numbers = list(map(int, input().split()))[:T]

# max = max(set(numbers))
# min = min(set(numbers))
sorted_numbers = sorted(numbers)
max = sorted_numbers[-1]
min = sorted_numbers[0]

print(min, max)