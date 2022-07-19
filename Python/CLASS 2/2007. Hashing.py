asclist = []
ascdict = {}
M = 31

for i in range(97, 123):
    asclist.append(chr(int(i)))

for j in range(1, 27):
    ascdict[asclist[j-1]]=j

N = int(input())
S = input()
S_list = list(S)

sum_ = 0
pow_ = 0

for k in S_list:
    sum_ += ascdict[k] * (M**pow_)
    pow_ += 1

print(sum_ % 1234567891)