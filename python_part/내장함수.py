#내장함수 : 내장되어 따로 import 할 필요없이 바로 사용가능한 함수
#input
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다".format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시하는 함수
print(dir())
import random #외장함수
print(dir())
import pickle
print(dir())

# print(dir(random)) # >> random 모둘 내에서 쓸 수 있는 것들을 표시함
# random. 할 때 뒤에 나오는 것들을 표시한다고 볼 수 있다

lst = [1,2,3]
print(dir(lst)) #lst에서 쓸 수 있는 것들이 표시됨

name = "Jim"
print(dir(name)) #>> name에 대해서 사용할 수 있는 정보들이 표시됨
