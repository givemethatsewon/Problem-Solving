word = input()

# r_word = word[::-1]

r_word = ''
for i in range(len(word)-1,-1,-1):
    r_word += word[i]

if word == r_word: print(1)
else: print(0)