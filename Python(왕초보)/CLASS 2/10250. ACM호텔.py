T = int(input())

for _ in range(T):
  h, w, n = map(int, input().split())

  list = []

  for row in range(1, w+1):
    for col in range(1, h+1):
      XX = str(col)

      if int(row) < 10:
        YY = "{0:02d}".format(row)
      else:
        YY = str(row)
      list.append(XX + YY)

  print(list[n-1])
