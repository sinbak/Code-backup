#지역변수 : 함수내에서만 사용가능 / 전역변수 : 어디서나 사용가능
gun = 10 #전역변수
def checkpoint(soldiers):
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers # 지역변수
    print("남은 총 : {0}개".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("남은 총 : {0}개".format(gun))
    return gun 
print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun,3) #함수 사용
print("남은 총 : {0}".format(gun))