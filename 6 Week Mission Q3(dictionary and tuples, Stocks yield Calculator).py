stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

stocks_list = stocks.split(",")
# print(stocks_list)

di = {}

for x in range(len(stocks_list)) :
    stocks_name = stocks_list[x].split("/")[0]
    buy_volume = stocks_list[x].split("/")[1]
    bid = stocks_list[x].split("/")[2]
    ask = sells[x]
    neto = (int(ask)-int(bid)) * int(buy_volume)
    stock_yield = neto / (int(bid)*int(buy_volume)) * 100
    di[stocks_name] = stock_yield

grading = sorted([(v,k) for k,v in di.items()],reverse=True)
for v,k in grading :
    print(f"{k}의 수익률 {v:.3}")
