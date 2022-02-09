# 당신의 학교에서는 파이썬 대회를 개최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다
# 댓글 작성자 중에서 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다
# 추천 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피당첨자 : [2,3,4,]
# -- 축하합니다 --

# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

from random import*
id = range(1,21) 
#print(type(id)) >> 형식 range는 list가 아니기에 리스트 함수 사용 x
id = list(id)
shuffle(id) #리스트 함수
win = sample(id,4) #4명 추출
print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(win[0]))
print("커피 당첨자 : {}".format(win[1:]))
print(" -- 축하합니다 --")