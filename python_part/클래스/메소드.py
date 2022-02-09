class unit:
    def __init__ (self,name,hp,damage): #__init__ : 파이썬에서 쓰이는 생성자
        self.name = name #self.변수명 >> 멤버변수 : 클래스 내에서 정의된 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))
#공격유닛
class attackunit:
    def __init__ (self,name,hp,damage): #__init__ : 파이썬에서 쓰이는 생성자
        self.name = name #self.변수명 >> 멤버변수 : 클래스 내에서 정의된 변수
        self.hp = hp #우측에 있는 것은 전달값을 바로 받아쓴다는 의미
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

#메딕 의무병


firebat1 = attackunit("파이어뱃", 50,16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)