n = int(input())

def digit_sum(n):
    n_list = []
    n_listSum = 0
    if n >= 1 and n <= 9999:
        for i in str(n):
            n_list.append(i)
        for num in n_list:
            n_listSum += int(num)
    print(n_listSum)

digit_sum(n)