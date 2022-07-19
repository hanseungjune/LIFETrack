x, y, w, h = map(int, input().split())

if w-x > x and h-y > y:
    if x > y:
        print(y)
    else:
        print(x)
elif w-x < x and h-y > y:
    if w-x > y:
        print(y)
    else:
        print(w-x)
elif w-x > x and h-y < y:
    if x > h-y:
        print(h-y)
    else:
        print(x)
else:
    if w-x > h-y:
        print(h-y)
    else:
        print(w-x)
