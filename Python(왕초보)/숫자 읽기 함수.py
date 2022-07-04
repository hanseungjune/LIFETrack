num = int(input())
num_str = ['일','이','삼','사','오','육','칠','팔','구','십']

def kr_num(num):
    for i in range(1, int(len(num_str))+1):
        if num_str[num-1] == num_str[i]:
            return num_str[num-1]
        else:
            continue

print(kr_num(num))