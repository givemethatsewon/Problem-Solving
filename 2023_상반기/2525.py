h,m = map(int,input().split())
m_need = int(input())

new_m = m+m_need

isRight = True
while isRight:
    if new_m >= 60:
        h += new_m//60
        new_m %= 60

    else: isRight = False 

if h >= 24:
    h %= 24
    
print(h, new_m)
