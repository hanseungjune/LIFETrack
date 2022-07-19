i = 0
multi = 1
multi_list = []

while i < 3:
    num = int(input())
    multi *= num
    i += 1

multi_list = list(str(multi))

for number in range(10):
    print(multi_list.count(str(number)))

# a = int(input())
# b = int(input())
# c = int(input())
#
# result = str(a * b * c)
#
# for i in range(10):                     #0~9까지 몇번 쓰였는지 알아볼거임
#     count = 0
#     for j in range(len(result)):        #첫번째 글자부터 끝까지 비교해보기
#         if result[j] == str(i):
#             count += 1
#     print(count)