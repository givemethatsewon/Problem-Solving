import sys
input = sys.stdin.readline

n = int(input())

def gcd(a,b):
    if b > a:
        while a != 0:
            b,a = a,b % a
        return b
    else:
        while b != 0:
            a,b = b,a % b
        return a

gaps = []
places = []
for i in range(n):
    place = int(input())   
    if i == 0:
        places.append(place)
    elif i == 1:
        gap = place - places[-1]
        places.append(place)
        gaps.append(gap)
    elif i == 2:
        gap = place - places[-1]
        factor = gcd(gaps[0],gap)
        places.append(place)
        gaps.append(gap)
    else:
        gap = place - places[-1]
        factor = gcd(factor,gap)
        places.append(place)
        gaps.append(gap)
    
tree = 0
for gap in gaps:
    tree += (gap//factor - 1)
print(tree)
