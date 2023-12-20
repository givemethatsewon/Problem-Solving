n = int(input())

for i in range(n):
    line = input().split()
    num = float(line[0])
    for j in range(len(line)):
        if line[j] == '@':
            num = num*3
        elif line[j] == '%':
            num = num+5
        elif line[j] == '#':
            num = num-7
    print('%0.2f'%num)
        