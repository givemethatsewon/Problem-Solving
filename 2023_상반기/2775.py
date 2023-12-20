#테스트 케이스 입력
t = int(input())

#재귀함수
def floor_stack(floor,layer=0):
    #base case
    global k
    if layer == k:
        return floor
    next_floor = []
    for idx in range(len(floor)):
        next_floor.append(sum(floor[:idx+1]))
    layer += 1
    return floor_stack(next_floor,layer)

#실행
for i in range(t):
    k = int(input())
    n = int(input())
    #base 형성제한
    base = [i for i in range(1,n+1)]
    print(floor_stack(base)[-1])

