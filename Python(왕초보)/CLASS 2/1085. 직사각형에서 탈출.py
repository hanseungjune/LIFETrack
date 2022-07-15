x, y, w, h = map(int, input().split())

if w//2 < x:
    if h//2 < y:
        boundary_x = w - x
        boundary_y = h - y
    else:
        boundary_x = w - x
        boundary_y = y
else:
    if h//2 < y:
        boundary_x = x
        boundary_y = h - y
    else:
        boundary_x = x
        boundary_y = y

if boundary_x <= boundary_y:
    min = boundary_x
else:
    min = boundary_y

print(min)