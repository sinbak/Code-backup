# coins = [500, 100, 50, 10]

# def big_coin(toPay, coins):
#     change_list = []
#     for coin in coins:
#         # change_list = [coin, toPay_last]
#         change_list.append([coin, toPay - coin])
#     biggest = change_list[0]
#     # biggest = [coin, toPay_last]
#     for change in change_list:
#         if biggest[1] >= 0:
#             break
#         elif biggest[0] > change[0]:
#             biggest = change
            
        
#     return biggest

# print(big_coin(34,coins))

# def coinCount(coin, m):
#     dp = [0 for _ in range(n+1)]



# def run_coinCount(coins,m):
#     from time import perf_counter
#     start = perf_counter()
#     answer = coinCount(coins,m)
#     finish = perf_counter()
#     print("coinCount([",coins[0],", ...],",m,") => ",answer,sep="")
#     print(round(finish-start, ndigits=6), "seconds")

# my_coins = [50,40,20,10,5,4,2,1]
# run_coinCount(my_coins,80)
# run_coinCount(my_coins,130)
# run_coinCount(my_coins,180)
# run_coinCount(my_coins,230)
# run_coinCount(my_coins,280)
# run_coinCount(my_coins,330)
# run_coinCount(my_coins,380)

# N, M = map(int, input().split())
# res = 0
# for i in range(N):
#   tmp = list(map(int, input().split()))
#   v = min(tmp)
#   res = max(res, v)
# print(res)

N = int(input())
s = [] #빈 리스트
for i in range(N):
  a, b = map(int, input().split())
  s.append([a, b]) #리스트에 추가

s.sort(key= lambda x: (x[1], x[0])) #끝나는 시간을 기준으로 정렬 (1,2) (2,2) (2,2)가 먼저 나오면 1,2는 나오지 못한다
print(s)
count = 0 #출력해야 할 값
e_time = 0 #
for j in range(N):
  if e_time <= s[j][0]: #시작시간과 끝나는 시간이 같을 수 있기 때문에 <=로 처리
    count += 1
    e_time = s[j][1] #갱신

print(count)
