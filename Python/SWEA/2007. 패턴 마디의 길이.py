T = int(input())

for i in range(1, T+1):
    txt = input()

    for j in range(1, 16):
        if txt[:j] == txt[j:j*2]:
            print(f'#{i} {j}')
            break