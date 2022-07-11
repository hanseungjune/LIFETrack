t = int(input())
for tc in range(t):
    t_cnt = int(input())
    document = ''
    for _ in range(t_cnt):
        word, digit = input().split()
        document += word * int(digit)

    print("#{}".format(tc+1))

    for i in range(0, len(document), 10):
        print(document[i:i+10])
