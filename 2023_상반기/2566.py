table = [list(map(int, input().split())) for i in range(9)]

nums = []
for row in table:
    nums += row
max_num = max(nums)

for row in table:
    try:
        c = row.index(max_num)
        print(max_num)
        r = table.index(row)
        print(r + 1, c + 1)
        break
    except ValueError:
        pass