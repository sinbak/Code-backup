# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end = " ") #이때 end는 끝날때 줄바꿈을 하지 않고 " " 대로 놔둔다는 뜻
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name,age,*language): #가변인자 >>> *변수명
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end = " ") #이때 end는 끝날때 줄바꿈을 하지 않고 " " 대로 놔둔다는 뜻
    for lang in language:
        print(lang, end= "")
    print() # 줄바꿈용도
    
profile("sin",20,"c","c++","java","python", "C#")
profile("joon",20,"c","c++")
