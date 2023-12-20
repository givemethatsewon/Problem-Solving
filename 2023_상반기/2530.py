h,m,s = map(int,input().split())
t = int(input())

new_s = s+t
if new_s >= 60:
    m = m + new_s//60
    new_s %= 60

if m >= 60:
    h = h + m//60
    m %= 60

if h >= 24:
    h %= 24

print(h,m,new_s)