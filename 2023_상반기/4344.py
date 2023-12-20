test_case = int(input())

for test in range(test_case):
    n_score = list(map(int, input().split()))
    n = n_score[0]
    scores = n_score[1:]
    mean = sum(scores)/n
    cnt = 0
    for score in scores:
        if score > mean:
            cnt += 1
    portion = cnt/n*100
    print(f'{portion:.3f}%')    
