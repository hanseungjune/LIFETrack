i = 0
multi = 1
multi_list = []

while i < 3:
    num = int(input())
    multi *= num
    i += 1

for s in str(multi):
    multi_list.append(s)

for number in range(0, 10):
    print(multi_list.count(str(number)))
