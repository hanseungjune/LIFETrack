number = int(input())
min_num = number - (len(str(number))*9)

if min_num < 0:
    min_num = 0

for i in range(min_num, number+1):
    digit = sum(list(map(int, str(i))))
    sum_ = i + digit
    if sum_ == number:
        print(i)
        break
    if i >= number:
        print(0)