num_list = []
for i in range(10):
    num_list.append(int(input()))
r_list = [n%42 for n in num_list]
set_list = set(r_list) 
print(len(set_list))
