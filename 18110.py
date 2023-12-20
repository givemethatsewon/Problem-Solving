import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    
else:
    #난이도 저장하기
    opinion = [int(input()) for _ in range(n)]
    #절사하기
    length = len(opinion)
    opinion.sort()  #정렬
    cut = int(length*0.15 + 0.5)
    cutted = opinion[cut:length-cut]
    #평균 구하기
    mean = int((sum(cutted) / len(cutted)) + 0.5)
    print(mean)