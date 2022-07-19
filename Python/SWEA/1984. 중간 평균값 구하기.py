T = int(input())

for _ in range(1, T+1):
    ten_list = list(map(int, input().rstrip().split()))[:10]
    ten_list2 = sorted(ten_list)
    ten_list2.remove(ten_list2[0])
    ten_list2.remove(ten_list2[-1])

    avg = sum(ten_list2)/len(ten_list2)
    print(f'#{_} {round(avg)}')