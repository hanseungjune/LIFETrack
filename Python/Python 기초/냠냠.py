word = input()               #주어진 단어

group = []                      #알파벳 전체 불러오기
for i in range(97, 123):
    group.append(chr(i))                #아스키코드 이용 chr(i): 아스키코드 i번 문자

for j in group:
    word_index = word.index(j)
    print(word_index)