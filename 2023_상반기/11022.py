t = int(input())
result_list = []
a_list = []
b_list = []
for i in range(t):
    a,b = map(int,input().split())
    result = a + b  
    result_list.append(result)
    a_list.append(a)
    b_list.append(b)
    
for i in range(t):
    case = i + 1
    print(f"Case #{case}: {a_list[i]} + {b_list[i]} = {result_list[i]}")