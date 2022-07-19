def read(text):
    ridename, cm = map(lambda x : x, text.split(':'))

    cmmin = cmmax = None
    if '~' in cm:
        cmmin, cmmax = map(lambda x: int(x.replace("cm", "")), cm.split("~"))
    elif "이상" in cm:
        cmmin = int(cm.split("cm")[0])

    return ridename, cmmin, cmmax

if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)