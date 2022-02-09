#pickle이란 프로그램상에서 사용하고 있는 데이터를 파일 형태로 저장하는 것
# import pickle
# profile_file = open("profile.pickle", "wb") #wb 중 b는 바이너리 형식을 뜻하며 pickle 사용할 시 필요
# profile = {"이름": "sin", "나이" : 22, "취미" : ["축구", "코딩", "독서"]}
# print(profile)
# #pickle을 이용해서 데이터를 파일에다 쓰는 것
# pickle.dump(profile,profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

import pickle
# profile_file = open("profile.pickle", "wb")
# profile = { "name": "sin", "age" : 22, "hobby":["soccer","coding","reading"]}
# print(profile)
# pickle.dump(profile,profile_file)
# profile_file.close()
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))
# #with를 사용하면 close()를 사용할 필요가 없다

with open("study.txt","w",encoding="utf8") as study_file: #파일명:study.txt, 파일정보를 study_file이라는 변수에 저장
    study_file.write("파이썬을 학습하는 중입니다")

with open("study.txt", "r", encoding= "utf8") as study_file:
    print(study_file.read())