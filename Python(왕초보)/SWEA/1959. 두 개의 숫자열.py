T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if n == m :
        max = 0
        for i in range(n):
            max += A[i] * B[i]
    else:
        if n > m :
            sum = [0] * (n-m+1)
            for i in range(len(sum)):
                for j in range(0, m):
                    sum[i] += A[j+i]*B[j]
        else :
            sum = [0] * (m-n+1)
            for i in range(len(sum)):
                for j in range(0, n):
                    sum[i] += A[j]*B[j+i]
    print("#{} {}".format(tc, max(sum)))