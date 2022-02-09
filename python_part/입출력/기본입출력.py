# print("java","python")
# print("java","pytnon",sep=",",end="?") #sep는 주 변수 사이 (띄어씐 부분)에 넣을 값을 지정/end 부분을 붙여서 두줄을 한줄로 바꿔줌
# print("무엇이 재미있을까요?")

# import sys
# print("python","java", file= sys.stdout) #sys.stdout : 표준출력
# print("python","java", file= sys.stderr) #sys.stderr : 표준에러

#출력포맷  /  시험성적
# scores = {"수학" : 0, "영어":50, "코딩" :100}
# for subject, scores in scores.items(): #items을 이용하여 key 와 value 모두를 가져온다
#     #print(subject,scores)
#     print(subject.ljust(8),str(scores).rjust(4), sep = ":") #.ljust() 란 왼쪽으로 정렬을 하되 ()안의 수만큼 공간을 확보한다는뜻

#은행 대기순번
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) #zfill() >> 0으로 채운다 ()안의 숫자는 얼마나 채울것인지 3이면 001

answer = input("아무값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " +answer + "입니다")
