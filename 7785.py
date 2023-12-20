import sys
input = sys.stdin.readline

n = int(input())
people_set = set()
for _ in range(n):
    name,state = input().split()
    if state == 'enter':
        people_set.add(name)
    else:
        people_set.remove(name)

people_list = list(people_set)
people_list.sort(reverse=True)
print(*people_list, sep='\n')