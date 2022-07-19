min_temper, max_temper = map(int, input().split())
temperture = map(int, input().split())

for i in temperture:
    if i >= min_temper and i <= max_temper:
        print('Nothing to report')
    else:
        if i == -999:
            break
        else:
            print('Alert!')
            break