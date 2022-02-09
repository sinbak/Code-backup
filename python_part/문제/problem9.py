# 동네에 항상 대기 손님이 있는 맛있는 치킨점이 있습니다
# 대기 손님의 치킨 요리시간을 줄이고자 자동주문시스템을 제작하였습니다
# 시스템코드를 확인하고 적절한 예외처리 구문을 넣으시오

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#     출력 메시지 : "잘못된 값을 입력하셨습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
class SoldOutError(Exception):
   pass

chicken = 10
waiting = 1 #홀 안에는 만석, 대기번호 1 부터 시작
while(True):
    try:
        print("남은 치킨 : {0}".format(chicken))
        order = int( input("치킨을 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        
        elif order <=0:
            raise ValueError #raise 에러명 >>> 발생시킬 에러를 raise를 이용한 뒤
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting,order))
            waiting +=1
            chicken -= order
        
        if chicken ==0:
            raise SoldOutError

    except ValueError: #except 에러명을 통해 에러발생 시 출력할 값을 설정한다
        print("잘못된 값을 입력하셨습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
        
