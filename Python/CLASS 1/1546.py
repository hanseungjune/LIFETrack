num = int(input())
score = list(map(int, input().split()))[:num]

max = max(score)
index = 0

for i in score:
    score[index] = (i / max) * 100
    index += 1

print(sum(score)/num)