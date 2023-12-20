import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nonhear = set()
nonseen = set()

for _ in range(n):
    name = input().rstrip()
    nonhear.add(name)

for _ in range(m):
    name = input().rstrip() 
    nonseen.add(name)

never = list(nonseen & nonhear)
never.sort()

print(len(never))
print(*never, sep='\n')

