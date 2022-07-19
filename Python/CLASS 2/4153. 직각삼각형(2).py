while True:
    triangle_list = list(map(int, input().split()))

    if sum(triangle_list) == 0:
        break

    max_num = max(triangle_list)
    triangle_list.remove(max_num)

    if max_num**2 != triangle_list[0]**2 + triangle_list[1]**2:
        print('wrong')
    elif max_num**2 == triangle_list[0]**2 + triangle_list[1]**2:
        print('right')