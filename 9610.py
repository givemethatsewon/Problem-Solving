#테스트 케이스 입력
t = int(input())
#변수 설정
q1 = q2 = q3 = q4 = axis = 0
#사분면/축 결정
for i in range(t):
    x, y = map(int, input().split())
    if x > 0 and y > 0: q1 += 1
    elif x < 0 and y > 0: q2 += 1
    elif x < 0 and y < 0: q3 += 1
    elif x > 0 and y < 0: q4 += 1
    else: axis += 1
#출력
print('Q1:',q1)
print('Q2:',q2)
print('Q3:',q3)
print('Q4:',q4)
print('AXIS:',axis)
