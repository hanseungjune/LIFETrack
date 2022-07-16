T = int(input())

for i in range(T):
    num, string = input().split()
    num = int(num)
    for i in range(len(string)):
        print(num * string[i], end="")
    print()
