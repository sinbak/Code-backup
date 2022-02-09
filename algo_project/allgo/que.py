# def coinCount(coin, m):
#   dp = [m]*(m+1)
#   dp[0] = 0
#   dir=[]
#   for j in range(1, m+1): #임시 거스름돈
#     for i in range(len(coin)): #액면이 가장 높은 동전부터 1원짜리 동전까지
#       if coin[i] <= j and dp[j-coin[i]] + 1 <= dp[j]:
#         dp[j] = dp[j-coin[i]] + 1 #최소의 동전 수

  
    
#   return dp[m]

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

def coin_count(coins, m):
    if m > 0:
        while len(coins) > 0 and m < coins[0]:
            coins = coins[1:]  # 지불 금액보다 더 큰 단위의 동전 제외

        if coins[0] > 1: 
            n1 = coin_count(coins[1:], m) # None대신 coins[0] 동전을 사용하지 않고 지불하는 경우 최소 코인 개수를 구하는 식 작성 함수 m값이 변하지 않는다
            n2 = coin_count(coins, m - coins[0]) + 1 # None대신 coins[0] 동전 1개 이상 사용해 지불하는 경우 최소 코인 개수를 구하는 식 작성 식 + 작성
            return min(n1, n2)
            
        else: # coins[0] == 1
            return m

    else: # m == 0
        return 0

def run_coin_count(coins,m):
    from time import perf_counter
    start = perf_counter()
    answer = coin_count(coins,m)
    finish = perf_counter()
    print("coin_count([",coins[0],", ...],",m,") => ",answer,sep="")
    print(round(finish-start, ndigits=6), "seconds")

my_coins = [50,40,20,10,5,4,2,1]

run_coin_count(my_coins,80)
run_coin_count(my_coins,130)
run_coin_count(my_coins,180)
run_coin_count(my_coins,230)
run_coin_count(my_coins,280) # 대략 5초 이상 걸릴 것이다
# run_coin_count(my_coins,330) # 이건 대략 10초 이상 걸릴 것이다
# run_coin_count(my_coins,380) # 여기서부턴 너무 오래 걸려서 제대로 실행하기 힘들 것
def solution(n):
    answer = ''
    while n > 0:			
        n, r = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer += str(r)
    return int(answer, 3)

def solution(n):
    answer = []
    result = 0
    while True:
        if n < 3:
            answer.append(n)
            break
        answer.append(n % 3)
        n = n // 3
    answer.reverse()
    for i in range(len(answer)):
        result += (answer[i] * (3 ** i))
    return result

import random
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i]+ numbers[j])
    answer.sort()
    return answer
