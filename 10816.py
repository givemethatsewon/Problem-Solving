n = int(input())
cards = map(int, input().split())
card_dic = dict()
m = int(input())
nums = map(int, input().split())

for card in cards:
    if card in card_dic.keys():
        card_dic[card] += 1
    else:
        card_dic[card] = 1

for num in nums:
    result = card_dic.get(num)
    if  result == None:
        print(0,end=' ')
    else:
        print(result, end=' ')