h, m = map(int, input().split())

if h > 0 and h <= 23:
    if m >= 45 and m <= 59:
        m -= 45
    elif m < 45 and m >= 0:
        h -= 1
        m += 15
else:
    if m >= 45 and m <= 59:
        m -= 45
    elif m < 45 and m >= 0:
        h = 23
        m += 15

print("{} {}".format(h, m))