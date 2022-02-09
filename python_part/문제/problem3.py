# 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예시 = http://naver.com
# 규칙1 : http://은 제외 > naver.com
# 규칙2 : 처음 만나는 점(.) 이후의 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자개수 + 글자내 'e'갯수 + "!"로 구성

# 예시 : 생성된 비밀번호 : nav51!

address = "http://naver.com"
a = address.find(".")
print("생성된 비민번호 : " + address[7:10]+ str(len(address[7:a])) + str(address.count("e")) + "!")


address = "http://naver.com"
ad_str = address.replace("http://", "")
ad_str = ad_str[:ad_str.index(".")]
#print(ad_str)
pwd = ad_str[:3] + str(len(ad_str)) + str(ad_str.count("e")) + "!"
print(pwd)
print("{0}의 비밀번호는 {1}입니다".format(address,pwd))

ads = input("url주소를 입력하시오\n")
ads = ads.replace("http://","")
