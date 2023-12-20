snack,cnt,cash = map(int,input().split())
need = snack*cnt - cash
if need <= 0: print(0)
else: print(need)