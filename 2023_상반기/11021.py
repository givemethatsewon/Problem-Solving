t = int(input())
result_list = []

for i in range(t):
    a,b = map(int,input().split())
    result = a + b  
    result_list.append(result)

for i in range(t):
    case = i + 1
    print(f"Case #{case}: {result_list[i]}")