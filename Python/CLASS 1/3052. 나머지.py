num = []
remain = []

for _ in range(10):
    num += list(map(int, input().split()))

for i in num:
    remain.append(int(i)%42)
print(len(set(remain)))