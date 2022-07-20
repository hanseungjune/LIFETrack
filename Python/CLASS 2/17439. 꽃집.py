# import itertools
#
# N, K = map(int, input().split())
# flower_set = list(map(int, input().split()))[:N]
# nCr_list = []
# result_list = []
#
# def combinations_cnt(N, K):
#     result3 = 1
#     for item3 in range(1, N+1, 1):
#         result3 *= item3
#
#     result2 = 1
#     for item2 in range(1, N-K+1, 1):
#         result2 *= item2
#
#     result1 = 1
#     for item1 in range(1, K+1, 1):
#         result1 *= item1
#
#     return int(result3/(result2*result1))
#
# for i in range(K, 0, -1):
#     nCr = itertools.combinations(flower_set, i)
#     nCr_list.append(list(nCr))
#
#     if i == K:
#         for j in range(combinations_cnt(N, K)):              # (A, B, C)로 빠질때 10가지임 / 5, 3
#             check_str = nCr_list[K-i][j]
#             flower_sample = flower_set[:]
#             sum_point = 0
#             for k in range(K):
#                 flower_sample.remove(check_str[k])
#             for l in range(N-K):
#                 sum_point += flower_sample[l]
#             result_list.append(sum(nCr_list[K-i][j])*K+sum_point)

from itertools import combinations
import itertools
from unittest import result  # 조합 쓸거임

n, k = map(int, input().split())

cost = list(map(int, input().split()))

# 인덱스로 가능한 리스트 생성
index_list = []
for q in range(1, n):
    index_list.append(q)

com = list(itertools.combinations(index_list, k - 1))
print(com)
result = []

for s in range(len(com)):
    use_index = com[s]
    if_first = 0
    sum_total = 0

    for p in range(len(use_index)):
        j = use_index[p]

        if if_first == 0:
            sum_total = sum_total + (sum(cost[:j]) * (j))
            if_first += 1
            remember = int(j)
        else:
            sum_total = sum_total + (sum(cost[remember:j]) * (j - remember))
            remember = int(j)

    sum_total = sum_total + (sum(cost[remember:n + 1]) * (n - remember))

    result.append(sum_total)

print(min(result))