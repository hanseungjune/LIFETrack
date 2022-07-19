dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

dice1_set = set(dice1)
dice2_set = set(dice2)
sum_set = set()

for i in dice1_set:
    for j in dice2_set:
        sum_set.add(int(i + j))

print(sum_set)