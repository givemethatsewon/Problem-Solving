import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = dict()
    for _ in range(n):
        cloth = input().split()[1]  #옷 종류
        if cloth in clothes:
            clothes[cloth] += 1
        else:
            clothes[cloth] = 1
        
    net = 1
    for cloth in clothes:
        net *= (clothes[cloth] + 1) #VALUE를 뽑아와서 리스트 만드는 것보다 이게 딕셔너리에서 바로 접근하는게 메모리 측면에서 이득
    print(net - 1) #알몸인 경우 제외
