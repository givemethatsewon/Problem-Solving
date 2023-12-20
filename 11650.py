import sys
input = sys.stdin.readline

n = int(input())
pairs = [list(map(int, input().split())) for i in range(n)]

#sort 메서드의 key 매개변수와 람다함수를 이용한 2차원 배열 정렬
#key: 함수의 결과에 따라 정렬을 할 수 있다
#lambda: 함수를 매개변수와 표현식만 써서 간략하게 쓸 수 있다
pairs.sort(key=lambda x : (x[0],x[1]))

for pair in pairs:
    print(*pair, sep=' ')
