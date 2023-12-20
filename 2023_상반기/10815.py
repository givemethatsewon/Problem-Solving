n = int(input())
cards = list(map(int, input().split()))
card_dic = dict()

#딕셔너리에 추가  key == card, value == 1
for card in cards:
    card_dic[card] = 1
#숫자들 받기
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    value = card_dic.get(num)
    if value == None:
        print(0, end=' ')
    else:
        print(value, end=' ')