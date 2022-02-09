def coin_count(coins, m):
    if m > 0:
        while len(coins) > 0 and m < coins[0]:
            coins = coins[1:]  # 지불 금액보다 더 큰 단위의 동전 제외
#m은 거스름돈
        if coins[0] > 1: 
            n1 = None # None대신 coins[0] 동전을 사용하지 않고 지불하는 경우 최소 코인 개수를 구하는 식 작성
            n2 = None # None대신 coins[0] 동전 1개 이상 사용해 지불하는 경우 최소 코인 개수를 구하는 식 작성
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

#2번문제 (표채워풀기)
def coinCount(coin, m):
    pass # 여기에 작성

def run_coinCount(coins,m):
    from time import perf_counter
    start = perf_counter()
    answer = coinCount(coins,m)
    finish = perf_counter()
    print("coinCount([",coins[0],", ...],",m,") => ",answer,sep="")
    print(round(finish-start, ndigits=6), "seconds")

run_coinCount(my_coins,80)
run_coinCount(my_coins,130)
run_coinCount(my_coins,180)
run_coinCount(my_coins,230)
run_coinCount(my_coins,280)
run_coinCount(my_coins,330)
run_coinCount(my_coins,380)

#3문제
def coin_pay(coin, m):
    if m > 0:
        while len(coins) > 0 and m < coins[0]:
            coins = coins[1:]  # 지불 금액보다 더 큰 단위의 동전 제외

        if coins[0] > 1: 
            pass # 여기에 적절한 코드 작성
        else: # coins[0] == 1
            return (m,{1:m}) # 총 m개의 동전이 필요하며 1짜리 동전 m개 사용해 지불
       
    else: # m == 0
        return (0,{}) # 지불해야 할 금액이 0으로 없으므로 필요한 동전도 0개고 함께 빈 map을 타나태는 {}를 리턴

def run_coin_pay(coins,m):
    from time import perf_counter
    start = perf_counter()
    answer = coin_pay(coins,m)
    finish = perf_counter()
    print("coin_pay([",coins[0],", ...],",m,") => ",answer,sep="")
    print(round(finish-start, ndigits=6), "seconds")

# 작성한 다음 아래 테스트를 돌려 보라
my_coins = [50,40,20,10,5,4,2,1]

run_coin_pay(my_coins,80)
run_coin_pay(my_coins,130)
run_coin_pay(my_coins,180)
run_coin_pay(my_coins,230)
run_coin_pay(my_coins,280) # 대략 5초 이상 걸릴 것이다
# run_coin_pay(my_coins,330) # 이건 대략 10초 이상 걸릴 것이다
# run_coin_pay(my_coins,380) # 여기서부턴 너무 오래 걸려서 제대로 실행하기 힘들 것