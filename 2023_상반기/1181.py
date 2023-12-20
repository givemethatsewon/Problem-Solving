import sys
input = sys.stdin.readline

n = int(input())
word_set = set()

for _ in range(n):
    word_set.add(input().rstrip())

# word_list = sorted(list(word_set))
# word_list.sort(key=len)
word_list = []
for word in word_set:
    word_list.append((len(word),word))
word_list.sort(key = lambda x : (x[0],x[1]))

for pair in word_list:
    print(pair[1])
