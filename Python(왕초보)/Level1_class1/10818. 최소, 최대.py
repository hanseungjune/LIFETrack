T = int(input())

numbers = list(map(int, input().split()))[:T]

max = max(set(numbers))
min = min(set(numbers))

print(min, max)