# 표준 체중을 구하는 프로그램을
# *표준체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) *22
# 여자 : 키(m) * 키(m) *21

# 조건: 표준 체중은 별도의 함수내에서 계산
#     함수명 : std_weight
#     전달값 : height,gender
# 조건2 : 표준체중은 소수점 둘째자리까지 표시

# 출력문
# 키 175cm 남자의 표준체중은 67.38kg입니다

def std_weight(height,gender):
    if gender == "남자":
        weight = (height/100)*(height/100) *22
        print("키 {0}cm {1}의 표준체중은 {2}kg입니다".format(height,gender,round(weight,2)))

    else:
        weight = (height/100)*(height/100)*21
        print("키 {0}cm {1}의 표준체중은 {2}kg입니다".format(height,gender,round(weight,2)))

std_weight(175,"남자")
std_weight(169,"여자")

#답안
def std_weight(height,gender):
    if gender == "남자":
        return height*height *22

    else:
        return height*height *22

height = 175
gender = "남자"
weight = round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준체중은 {2}kg입니다".format(height,gender,weight))