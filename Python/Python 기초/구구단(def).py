# num = int(input('몇단까지 출력할까요? '))
# print('1단부터 {}단까지'.format(num))
def gugudan(num):
    for i in range(1, num+1):
        for j in range(1, 10):
            print('{} x {} = {}'.format(i, j, i*j))

gugudan(4)