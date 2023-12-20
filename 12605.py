import sys

test_case = int(sys.stdin.readline())
for case in range(1,test_case+1):
    sent = sys.stdin.readline().split()
    print(f'Case #{case}:', end=' ')
    
    while len(sent) > 0:
        print(sent.pop(), end=' ')
    print()
    