cnt = int(input())

def middle_num(cnt):
    num_list = list(map(int, input().split()))[:cnt]
    num_list.sort()
    return print(num_list[cnt//2])

middle_num(cnt)

