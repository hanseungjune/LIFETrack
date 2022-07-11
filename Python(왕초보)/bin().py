num = int(input())
binary_int = []

def binary_change(num):
    binary_arr = list(bin(num))[2:]
    for i in binary_arr:
        binary_int.append(int(i))

    print(binary_int)

binary_change(num)