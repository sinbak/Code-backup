# def profile (name,age,main_lang):
#     print("이름 : {0}\t나이 : {1}\t주언어 : {2}".format(name,age,main_lang))

# profile("sin",22,"python")
# profile("joon",22,"java")

#같은반 같은 나이 같은 반 같은 수업
def profile (name,age=22,main_lang="python"):
    print("이름 : {0}\t나이 : {1}\t주언어 : {2}".format(name,age,main_lang))

profile("sin")
profile("joon")