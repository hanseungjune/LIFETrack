from datetime import datetime
today = datetime.today()
year = int(input())

def korean_age(year):
    return today.year - year + 1

print(korean_age(year))