A,B = map(int, input().split())
x = max(A,B)
y = min(A,B)

# def gcd(a,b):
#     while b != 0:
#         a,b = b,a % b
#     return a
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a % b)

print(x * y // gcd(x,y))