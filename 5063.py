t = int(input())
result = []

for i in range(t):
    r, e, c = map(int, input().split())
    
    if r < e - c: result.append('advertise')
    elif r > e - c: result.append('do not advertise')
    else: result.append('does not matter')

for i in result:
    print(i)