# weather = input("오늘 날씨는 어때요? ")
# if weather == "rain":
#     print("Get your unbrella")
# elif weather == "smoke":
#     print("Get your mask")
# else:
#     print("Don't have to get anything")

#input은 항상 문자열이므로 상황에 맞게 값형태 설정

temp = int(input("기온은 어때요? "))
if 30<= temp:
    print("너무 더워요 외출자제")
elif 10<= temp and temp < 30:
    print("괜찮은 날씨입니다")
elif 0<=temp and temp<10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")