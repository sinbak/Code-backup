# for wait_num in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(wait_num))

#randrange
for wait_num in range(1,6):
    print("대기번호 : {0}".format(wait_num))

starbucks = ["아이언", "톨","나무"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))

#while
customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer,index))
    index -= 1 #하나씩 줄여나간다
    if index == 0:
        print("커피는 폐기처분되었습니다")


# cust = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer,index))
#     index +=1
# #>> 무한루프

cust = "토르"
person = "unknown"

while person != customer: 
    print("{0}, 커피가 준비 되었습니다".format(cust))
    person = input("이름이 어떻게 되세요?")

    