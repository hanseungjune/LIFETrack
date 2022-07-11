colwidth = 79
rule90 = {'111':'0',
          '110':'1',
          '101':'0',
          '100':'1',
          '011':'1',
          '010':'0',
          '001':'1',
          '000':'0'
          }

half = colwidth // 2
line = half * '0' + '1' + half * '0'

while line[1] == '0':
    prev = line
    line = '0' * colwidth
    for i in range(1, colwidth - 1):
        line = line[:i] + rule90[prev[i-1:i+2]] + line[i+1:]
    print(line)
