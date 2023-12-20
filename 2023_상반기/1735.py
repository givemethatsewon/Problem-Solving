a,b = map(int, input().split())
c,d = map(int, input().split())
x1 = x = a*d + b*c
y1 = y = b*d

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

if x > y:
    n = gcd(x,y)
else:
    n = gcd(y,x)

result_x = x1 // n
result_y = y1 // n

print(result_x, result_y)