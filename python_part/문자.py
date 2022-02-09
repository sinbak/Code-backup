sentence = """
파이썬은 간단합니다
취미는 코딩입니다
"""
print(sentence)

#슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:])
print( "뒤 7자리 : " + jumin[-7:])
#맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)

print(python.find("n")) # find 는 찾을 값이 없는 경우 -1을 반환한다
#index 인 경우 에러가 뜸
print(python.count("n"))

print("나의 나이는 %d살 입니다" % 22)
print("%s을 공부하고 있습니다" % "python")
print("Apple은 %c로 시작합니다" % "A")
print("나는 %s 과 %s을 좋아합니다" % ("파란색", "빨강색"))

print("나는 {}살입니다".format(22))
print("나는 {} 과 {}을 좋아합니다".format("파란색", "빨강색"))
print("나는 {0} 과 {1}을 좋아합니다".format("파란색", "빨강색"))
print("나는 {age}살이며 {color}을 좋아합니다".format(age=22, color = "빨간색"))

age = 22
color = "red"
print(f"나는 {age} 이고 {color}를 좋아합니다")