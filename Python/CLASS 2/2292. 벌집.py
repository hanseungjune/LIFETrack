n = int(input())  # 몇번방까지 만들꺼야?
room_cnt = 1    # 현재 방 갯수
i = 1           # 거쳐간 방 갯수

while room_cnt < n:
    room_cnt += 6*i
    i += 1

print(i)
