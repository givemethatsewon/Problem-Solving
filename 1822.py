nA, nB = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

diff = a - b
diff_list = list(diff)
diff_list.sort()
count = len(diff_list)

if count:
    print(count)
    print(*diff_list, sep=' ')
else:
    print(0)