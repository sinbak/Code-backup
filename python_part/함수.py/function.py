def open_account():
    print("새로운 계좌를 생성되었습니다.")

def deposit(balance,money): #가로안에는 전달할 값을 넣는다
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance+money))
    return balance + money

def withdraw(balance,money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance-money
    
def withdraw_night(balance,money):
    commission = 100
    return commission, balance-money-commission

balance = 0
balance = deposit(balance,1000)
# print(balance)
# balance = 5000
# balance = withdraw(balance,2000)
# print(balance)
commission, balance = withdraw_night(balance,500) #수수료와 잔액을 넣는다
print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commission,balance))
#open_account() 