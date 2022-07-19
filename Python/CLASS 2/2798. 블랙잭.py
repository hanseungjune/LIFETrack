
# N, M = map(int, input().split())    # 카드의 개수, 넘으면 안되는 수
# card_list = list(map(int, input().split()))     # 카드 목록
# answer_list = []
#
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             three = card_list[i] + card_list[j] + card_list[k]
#             if three > M:
#                 continue
#             else:
#                 answer_list.append(three)
# print(max(answer_list))

# itertools combination(조합 사용)

from itertools import combinations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
sum_list = []

for three in combinations(card_list, 3):
    if sum(three) > M:
        continue
    else:
        sum_list.append(sum(three))
print(max(sum_list))

