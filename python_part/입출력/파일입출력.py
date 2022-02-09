# score_file = open("score.txt", "w", encoding = "utf8") # "w" = write(쓰기)
# print("math = 0",file=score_file)
# print("english = 50",file=score_file)
# print("coding = 100", file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding = "utf8") #이어쓰기(추가)를 할 때 append를 의미하는 "a"
# score_file.write("과학 : 80") # .write는 줄바꿈이 따로 안하기 때문에 
# score_file.write("\n국어 : 70") #\n을 추가하여야 한다
# score_file.close()

###### 파일 읽어오기

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read()) #전체를 읽어들인다
# score_file.close()

#####한줄한줄 읽어들여 처리하고 싶을 때
# score_file = open("score.txt","r",encoding = "utf8")
# print(score_file.readline()) #줄별로 읽기 동작/커서는 다음 줄로 이동
# #줄바꿈을 하기 싫을 때
# print(score_file.readline, end = "")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

#가져올 파일의 줄 수를 모르는 경우
score_file = open("score.txt", "r", encoding="utf8")
while True: #true 인 동안
    line = score_file.readline()
    if not line :
        break
    print(line)
    #줄바꿈을 하기 싫을 때 print(line, end = "")
score_file.close()

score_file = open("score.txt", "r", encoding= "utf8")
lines = score_file.readlines() #리스트 형태로 저장
for line in lines:
    print(line, end = "")