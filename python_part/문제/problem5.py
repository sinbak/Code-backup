# 당신은 cocoa 서비스를 이용할는 택시기사입니다.
# 50명의 승객과 매칭 기회가 잇을 때, 총 탑승 승색 수를 구하는 프로그래을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다
# 조건2 : 당신은 소요 시간은 5분~15분 사이의 승객만 매칭해야합니다

# 출력문
# [O] 1번쨰 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2분

from random import*
person = 0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <=15:
#         print("[O] {0}번째 손님 (소요시간 : {1})".format(i,time))
#         person +=1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1})".format(i,time))
# print("총 탑승 승객 : {}분".format(person))
i = 1
while i <=50: #for in range를 사용하면 좀더 보기좋게 작성 가능
    time = randint(1,51)
    if 5 <= time and time <=15:
         print("[O] {0}번째 손님 (소요시간 : {1})".format(i,time))
         i+=1
         person +=1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i,time))
        i+=1
print("총 탑승 승객 : {}분".format(person))