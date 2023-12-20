bowl = input()
h = 10
n_bowl = bowl[1:]

for i in range(len(n_bowl)):
    if bowl[i] == n_bowl[i]: h += 5
    else: h += 10
print(h)
