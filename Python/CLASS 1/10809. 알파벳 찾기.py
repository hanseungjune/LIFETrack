# word = input()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
#
# for i in alphabet:
#     if i in word:
#         print(word.index(i), end=" ")
#     else:
#         print(-1, end=" ")

x = input()
y = list(range(97, 123))

for i in y:
    print(x.find(chr(i)), end=" ")