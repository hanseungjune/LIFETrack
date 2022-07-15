i = 0
list = []

while i < 9:
    list.append(int(input()))
    i += 1

list_set = set(list)
max = max(list_set)

print(max)
print(list.index(max)+1)