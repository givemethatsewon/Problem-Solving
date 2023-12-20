test_case = int(input())

for t in range(test_case):
    isRight = True
    cnt = 0
    h, w, n = map(int, input().split())
    
    for i in range(1, w+1):
        if isRight == False: 
            break
        else:
            i = str(i)
            if len(i) == 1: 
                i = '0' + str(i)
            else:
                pass
            
        for j in range(1, h+1):
            room = str(j) + i
            cnt += 1
            if cnt == n:
                print(room)
                isRight = False
                