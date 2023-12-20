#입력
a,b,v = map(int, input().split())
#알고리즘
x = (v-a) % (a-b)
if x > 0:
    result = (v-a) // (a-b) + 2
else:
    result = (v-a) // (a-b) + 1
#출력
print(result)