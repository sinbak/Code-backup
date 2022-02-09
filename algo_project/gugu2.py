result = 0
for n in range(1,1000):
    if n%3 == 0 or n%5 == 0:
        result += n
print(result)

#3과 5의 배수 합하기

# n = int(input("값을 입력하시오 : "))
# for i in range(1,n):
#     if n ==0:
#         print("다시 입력하세요")
#         continue
#     else:
#         print(i,end=" ")

in_num = [i*i2 for i in range(2,10)
for i2 in range(1,10)]
print(in_num) # for문을 중첩해서 사용

a = [1,2,3,4]
result = [num * 5 for num in a]
print(result)

def self_gugu(i,i2):
    for i in range(2,i2):
        if i2 <=2:
            print("2이상의 숫자를 입력하시오")
        else:
            result = i*i2
            print(result, end=" ")

def f (x,y,**kwargs):
    return f

f(1,2,mode="fast", header="debug")
self_gugu(4,7)

def func_param_with_kwargs(name, age, address=0, **kwargs): #**kwargs : 키워드
    print("name=",end=""), print(name)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)

func_param_with_kwargs("sh", 12, "seoul", mobile="010123456789")   #딕셔너리 처럼 출력

#정답
def mixed_params(age, name="아이유", *args, address, **kwargs):
    print("age=",end=""), print(age)
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("address=",end=""), print(address)
    print("kwargs=",end=""), print(kwargs)
#오류
def mixed_params(name="아이유", *args, age, **kwargs, address):
    print("name=",end=""), print(name)
    print("args=",end=""), print(args)
    print("age=",end=""), print(age)
    print("kwargs=",end=""), print(kwargs)
    print("address=",end=""), print(address)
mixed_params(20, "정우성", "01012341234", "male" ,mobile="01012341234", address="seoul")





        




