subway = [10,20,30] # 리스트
# subway = 10
# subway = 20
# subway = 30
print(subway)

subway = ["나도코딩","조코딩","이고잉"]
print(subway)
print(subway.index("조코딩"))

#shin 이 다음역에서 탐
subway.append("shin")
print(subway)
#joon 을 조코딩과 이고잉 사이에 넣어는다
subway.insert(1,"joon")
print(subway)

#한명씩 꺼내기
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇 명 있는지 확인
subway.append("이고잉")
print(subway)
print(subway.count("이고잉"))

#정렬
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

#순서 뒤집기
# num_list.reverse()
# print(num_list)

#모두 지우기
# num_list.clear()
# print(num_list)

#다양한 자료형과 함께
num_list = [5,2,4,3,1]
mix_list = ["조세",1, True]
print(mix_list)
num_list.extend(mix_list) #가로안의 값을 
print(num_list) #여기에 확장한다 >> 하나의 리스트로 합치기


square = list(map(lambda x : x**2, range(10)))
print(square)

com = [x**2 for x in range(10)]
print(com)

