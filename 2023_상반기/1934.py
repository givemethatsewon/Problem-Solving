import sys
from copy import deepcopy
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    if b > a:
        a,b = b,a
    a_origin = deepcopy(a)
    b_origin = deepcopy(b)
    while True:
        r = a % b
        if r == 0:
            break
        a = b
        b = r
    #b가 최대공약수
    print(a_origin * b_origin // b)
    
    