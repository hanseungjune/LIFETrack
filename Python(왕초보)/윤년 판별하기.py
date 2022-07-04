while True:
    is_leap_year = None

    year = int(input('입력년도는 윤년일까? : '))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    if is_leap_year:
        print(("{0}년은 윤년입니다.").format(year))
    else:
        print(("{0}년은 평년입니다.").format(year))