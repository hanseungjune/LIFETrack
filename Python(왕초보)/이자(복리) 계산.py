prin = int(input('원금은 얼마인가? '))
rate = float(input('이자율은 얼마인가? '))
time = int(input('기간은 얼마인가? '))
num = 4

def compound_interest_amount():
    return int(prin * ((1+rate/num)**(num*time)))

print('원리금은 {}원이다.'.format(compound_interest_amount()))