#메소드 오버라이딩이란 부모클래스에서 정의한 내용말고 자식 클래스에서 정의한 메소드를 쓰고 싶을 때



class unit:
    def __init__ (self,name,hp,speed): #__init__ : 파이썬에서 쓰이는 생성자
        self.name = name #self.변수명 >> 멤버변수 : 클래스 내에서 정의된 변수
        self.hp = hp
        self.speed = speed

    def move(self,location): #unit 클래스에 move()함수를 추가
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name,location,self.speed))

     
#공격유닛
class attackunit(unit):
    def __init__ (self,name,hp,speed,damage): #__init__ : 파이썬에서 쓰이는 생성자
        unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

#드랍쉽 : 공중 유닛,수송기/공격x
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self,name,location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name,location,self.flying_speed))

#공중공격 유닛
class flyableattackunit(attackunit, flyable):
    def __init__(self,name,hp,damage,flying_speed):
        attackunit.__init__(self,name,hp,0,damage) #지상스피드는 0
        flyable.__init__(self,flying_speed)

    def move(self,location): #move() 함수를 새롭게 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name,location) #flyable의 클래스의 fly함수 이용

#벌쳐 : 지상유닛,기동성 좋음
vulture = attackunit("vultue",80,10,20)

#배틀크루저 : 공중유닛
battlecruiser = flyableattackunit("배틀크루저",500,25,3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")
