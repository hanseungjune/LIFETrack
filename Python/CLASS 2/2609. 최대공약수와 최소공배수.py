a, b = map(int, input().split())
aa, bb = a, b

if a > b:
    while b != 0:
        remains = a%b
        a, b = b, remains
else:
    while a != 0:
        remains = b%a
        b, a = a, remains

gcd = a or b
lcm = (aa * bb) // gcd
    
print(gcd)
print(lcm)
