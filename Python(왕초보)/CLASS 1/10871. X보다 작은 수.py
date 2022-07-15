num, x = map(int, input().split())

if num >= 1 and x <= 10000:
    list = list(map(int, input().split()))
    answer_list = ""

    for i in list:
        if x > int(i):
            answer_list += "{} ".format(int(i))

    print(answer_list)