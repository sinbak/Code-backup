#사전에서는 키에 대한 중복은 허용 X
cabinet = {3:"유재석", 100 : "조세호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])  이런식으로는 에러 출현후 다음 명령이 실행이 안 되지만

print(cabinet.get(5, "사용 가능")) #get을 사용한 경우 none 값을 반환하고 뒤 명령문을 실행(5 옆은 에러 떳을시의 출력값)

print("hi")

print(3 in cabinet) # 3이 cabinet에 있는지 확인 (true/false)

cab = {"a-3" : "code", "b-3" : "reading"}
print(cab["a-3"])
print(cab["b-3"])
#키와 값을 수정 및 추가할 때
cab["c-3"] = "listening" # 사전에 키와 값을 추가
cab["a-3"] = "marking" # a-3 키의 값을 marking으로 바꿈

print(cab)
#값 지우기
del cab["a-3"]  #del 은 딕셔너리에 있는 선택한 부분을 삭제
print(cab)

#사용하는 키들을 표시
print(cab.keys())
#value 만 표시
print(cab.values())
#key 와 value 를 한 쌍으로 출력
print(cab.items())

cab.clear()
print(cab)

club = { "cap" : "jh", "sub" : "lg", "money" : "ls"}
print(club["cap"])
club["cap"] = "ig"
print(club)

