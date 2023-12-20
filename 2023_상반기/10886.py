N = int(input())
cute = []
notcute = []

for i in range(N):
    opn = int(input())
    if opn == 1:
        cute.append(opn)
    else:
        notcute.append(opn)
    
if len(cute) > len(notcute):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')