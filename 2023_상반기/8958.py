t = int(input())
for i in range(t):
    ox = input()
    score = 0
    ox = ox.split('X')

    for data in ox:
        n = len(data)
        sigma = n*(n+1)/2
        score += int(sigma)
    print(score)
    
    