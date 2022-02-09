menu = ("돈까스", "치즈김밥")
print(menu[0])
print(menu[1])

#menu.add("김치") >튜플에서는 추가,변경이 불가능

# name = "한"
# age = 22
# hobby = "코딩"
# print(name,age,hobby)

(name, age, hobby) = ("한",22,"coding")
print(name,age,hobby)
#==========================================================================================
#집합 set
#중복 안됨, 순서 X
my_set = {1,2,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}  #튜플은 () 리스트는 [] 딕셔너리는 {}
python = set(["유재석","박명수"])

#교집합
print(java&python) 
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java-python)
print(java.difference(python))

#추가
python.add("김태")
print(python)

#제거
java.remove("김태호")
print(java)

club = ("jh", "ig", "sh", "hs")
# club.add("yy")
print(club)

cl = {"jh", "ig", "sh", "hs", "hs"} #set을 사용할 때는 튜플과 다르게 {}를 사용한다
print(cl)
cl.add("yy")
print(cl)
