print('input()을 사용해 사용자로부터 입력받은 숫자를 한글로 출력하는 프로그램을 작성하세요. 단, 사용자는 1 이상 3 이하의 정수 중 하나를 입력한다고 가정합니다.')
num = int(input('1 ~ 3에 해당하는 정수를 입력하시오 : '))

if num==1 :
    print('일')
elif num==2 :
    print('이')
elif num==3 :
    print('삼')
else:
    print('변환가능한 숫자가 아닙니다.')
