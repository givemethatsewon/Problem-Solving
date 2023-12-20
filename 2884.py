h,m = map(int,input().split())

if m >= 45: print(h,m-45)
else:
    m = 60-abs(m-45)
    h = h-1
    if h >= 0: print(h,m)
    else: print(24+h,m)
