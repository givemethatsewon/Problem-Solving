n = int(input())
word = input()

nums = [i for i in range(1,27)]
letters  = [chr(i) for i in range(97,123)]
pack = zip(letters,nums)

asc = {k:v for k,v in pack}

total = 0
for i in range(n):
    total += (asc[word[i]] * 31**i)

m = 1234567891
print(total % m)