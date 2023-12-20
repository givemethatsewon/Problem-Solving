all_list = [i for i in range(1,31)]
for i in range(28):
    n = int(input())
    all_list.remove(n)
print(*all_list, sep='\n')
