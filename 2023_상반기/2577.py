a = int(input())
b = int(input())
c = int(input())
result = str(a*b*c)

for n in range(0,10):
    print(result.count(str(n)))