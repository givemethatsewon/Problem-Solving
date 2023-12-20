acheive = input()
def plusminus(x):
    if '+' in acheive: print(x+0.3)
    elif '0' in acheive: print(x)
    else: print(x-0.3)

if 'A' in acheive: plusminus(4.0)
elif 'B' in acheive: plusminus(3.0)
elif 'C' in acheive: plusminus(2.0)
elif 'D' in acheive: plusminus(1.0)
else: print(0.0)

