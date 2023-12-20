import sys

t = int(sys.stdin.readline())

cache = {0:0, 1:1}

for _ in range(t):
    n = int(sys.stdin.readline())
    zero_cnt = {'first':1, 'second':0}
    one_cnt = {'first':0, 'second':1}
    
    if n == 0: print(zero_cnt['first'], one_cnt['first'])
    elif n == 1: print(zero_cnt['second'], one_cnt['second'])
    else:
        x = 2
        while n >= x: 
            cache[x] = cache[x-1] + cache[x-2] 
            # 0贸府
            zero_temp = zero_cnt['second']
            zero_cnt['second'] = zero_cnt['first'] + zero_cnt['second']
            zero_cnt['first'] = zero_temp
            # 1贸府
            one_temp = one_cnt['second']
            one_cnt['second'] = one_cnt['first'] + one_cnt['second']
            one_cnt['first'] = one_temp
            x += 1
        
        print(zero_cnt['second'], one_cnt['second'])