T = int(input())

for _ in range(1, T+1):
    num = int(input())
    calculation = 0
    for i in range(1, num+1):
        if i % 2 == 1:
            calculation += i
        else:
            calculation -= i
    print(f'#{_} {calculation}')