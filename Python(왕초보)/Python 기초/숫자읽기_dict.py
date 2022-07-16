num = int(input())

def korean_number(num):

    number_str = \
    {
        1: "일",
        2: "이",
        3: "삼",
        4: "사",
        5: "오",
        6: "육",
        7: "칠",
        8: "팔",
        9: "구",
        10: "십",
    }

    print(number_str[num])

korean_number(num)

