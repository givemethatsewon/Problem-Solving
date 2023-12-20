sentence = input().strip()
cnt = 1

if sentence:
    for letter in sentence:
        if letter == ' ': cnt += 1
    print(cnt)
else: print(0)
