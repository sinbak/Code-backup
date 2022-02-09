#출석번호 1,2,3,4 앞에 100을 붙이기로 함
# student = [1,2,3,4,5]
# students = [i+100 for i in student]
# print(students)

#학생의 이름을 길이로 변환
# students = ["iron", "tho","grove"]
# students = [len(i) for i in students]
# print(students)

#학생 이름을 대문자로 변환
students = ["iron", "tho","grove"]
students = [i.upper() for i in students]
print(students)

lis = []
a = input("목록을 입력하시오 : ")
lis.append(a)
print(lis)   #리스트를 입력하여 출력을 하려는 경우 append를  이용하여 출력을 해야한다 
