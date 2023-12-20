#입력
x, y, w, h = map(int, input().split())
#알고리즘
length = [w-x, h-y, x, y]
print(min(length))
