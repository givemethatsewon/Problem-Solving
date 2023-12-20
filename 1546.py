from decimal import Decimal as d

n = int(input())
scores = list(map(int, input().split()))    #점수 리스트
best_score = max(scores)    #최고점
sum_score = 0

for score in scores:
    sum_score += d(score)/d(best_score)*d(100)

new_mean = d(sum_score)/d(n)
print(new_mean)