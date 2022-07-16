T = int(input())

for _ in range(1, T+1):
    number = int(input())
    sales = list(map(int, input().split()))
    profit = 0

    max = sales[-1]
    for i in range(len(sales)-1,-1,-1):
        if sales[i] >= max:
            max = sales[i]
        profit += max - sales[i]
    print("#{} {}".format(_,profit))