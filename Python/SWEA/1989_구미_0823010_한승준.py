word_cnt = int(input())
word_list = []

for i in range(word_cnt):
    word = input()
    word_list.append(word)

for idx in range(word_cnt):
    word_unit = list(map(str, word_list[idx]))
    reverse_unit = list(reversed(word_unit))

    if word_unit == reverse_unit:
        print("#{}".format(int(idx) + 1), "1")
    else:
        print("#{}".format(int(idx) + 1), "0")
