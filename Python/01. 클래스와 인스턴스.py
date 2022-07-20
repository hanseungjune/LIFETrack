# print(list(range(5, 0, -1)))

# ------------------------

# flower_set = list(map(int, input().split()))[:5]
# a = (1, 1, 5)

# for i in range(3):
#     flower_set.remove(a[i])

# print(flower_set)

# ------------------------

# dust = 80
# if dust > 150:
#     print('매우 나쁨')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# else:
#     print('좋음')
# print('미세먼지 확인 완료')

# '''
# 보통
# 미세먼지 확인 완료!
# '''

# ----------------------

# num = 2
# result = '홀수입니다.' if num % 2 else '짝수입니다.'
# print(result)

# # 짝수입니다.

# ----------------------

# while 조건 = True:
#     run
#     break

# ----------------------

# a = 0
# while a < 5:
#     print(a)
#     a += 1
# print('끝')

# ----------------------

# for fruit in ['apple','mango','banana']:
#     print(fruit)
# print('끝')

# '''
# apple
# mango
# banana
# 끝
# '''

# ----------------------

# chars = input()

# for char in chars:
#     print(char)

# or

# for idx in range(len(chars)):
#     print(chars[idx])

# '''
# h
# a
# p
# p
# y
# '''

# ----------------------

# grades = {'john':80, 'eric':90}
# for student in grades:
#     print(student)

# '''
# john
# eric
# '''

# for student in grades:
#     print(student, grades[student])

# '''
# john 80
# eric 90
# '''
# ----------------------

# grades = {'john':80, 'eric':90}
# print(grades.keys())
# print(grades.values())
# print(grades.items())

# '''
# dict_keys(['john', 'eric'])
# dict_values([80, 90])
# dict_items([('john', 80), ('eric', 90)])
# '''

# for student, grade in grades.items():
#     print(student, grade)

# '''
# john 80
# eric 90
# '''

# ----------------------

# members = ['민수','영희','철수']

# for idx, number in enumerate(members):
#     print(idx, number)

# '''
# 0 민수
# 1 영희
# 2 철수
# '''

# ----------------------

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons)))
# print(list(enumerate(seasons, start=1)))

# '''
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
# '''

# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1
# print(enumerate(seasons, start=0))

# ----------------------

# 1~3의 세제곱 리스트 만들기
# cubic_list = []
# for number in range(1, 4):
#     cubic_list.append(number ** 3)
# print(cubic_list)

# cubic_list = [ number ** 3 for number in range(1, 4)]
# print(cubic_list)

# ----------------------

# 1~3의 세제곱 딕셔너리 만들기
# cubic_dict = {}

# for number in range(1, 4):
#     cubic_dict[number] = number ** 3
# print(cubic_dict)

cubic_dict = { number: number ** 3 for number in range(1, 4)}
print(cubic_dict)

# ----------------------
# ----------------------
# ----------------------
# ----------------------
# ----------------------