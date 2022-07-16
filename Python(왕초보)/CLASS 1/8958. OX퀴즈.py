T = int(input())

for _ in range(T):
    result = list(map(str, input()))
    score = 1
    total = 0
    for i in result:
        if i == 'O':
            total += score
            score += 1
        else:
            score = 1
    print(total)
