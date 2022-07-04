prin = int(input('원금은 얼마인가? '))
rate = float(input('이자율은 얼마인가? '))
time = int(input('기간은 얼마인가? '))

def simple_interest(prin, rate, time):
    return int(prin * rate * time)

def simple_interest_amount(prin, rate, time):
    return int(prin * (1 + rate*time))

print(simple_interest(prin, rate, time))
print(simple_interest_amount(prin, rate, time))