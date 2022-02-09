#메소드 오버라이딩이란 부모클래스에서 정의한 내용말고 자식 클래스에서 정의한 메소드를 쓰고 싶을 때
from random import*

class unit:
    def __init__ (self,name,hp,speed): #__init__ : 파이썬에서 쓰이는 생성자
        self.name = name #self.변수명 >> 멤버변수 : 클래스 내에서 정의된 변수
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self,location): #unit 클래스에 move()함수를 추가
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <= 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

     
#공격유닛
class attackunit(unit):
    def __init__ (self,name,hp,speed,damage): #__init__ : 파이썬에서 쓰이는 생성자
        unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(self.name,location,self.damage))

#마린
class marine(attackunit):
    def __init__(self):
        attackunit.__init__(self,"마린",40,1,5)
    #스팀팩 : 일정시간동안 이동/공격속도 증가,체력 10감소
    def stimpack(self):
        if self.hp >=10:
            self.hp -=10
            print("{0} : 스팀팩을 사용합니다.(hp 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
        
#탱크
class Tank(attackunit):
    #시즈모드 : 탱크 고정 및 공격력 증가,이동불가
    seize_developed = False #시즈모드 개발여부
    def __init__(self):
        attackunit.__init__(self,"탱크",150,1,35)
        self.seize_mode = False
#시즈모드를 한다그러면
    def set_seize_mode(self):
        if Tank.seize_developed == False:#시즈개발여부를 쓰기위해서
            return #시즈개발이 안 되어있을 경우 아무것도 안하고 그냥 나간다
        #현재 시즈모드가 아닐때 > 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seize_mode = True
        #시즈모드가 일때 > 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage *=2
            self.seize_mode = False

#공중유닛
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

#레이스
class Wraith(flyableattackunit):
    def __init__(self):
        flyableattackunit.__init__(self,"레이스",80,20,5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked = True


#드랍쉽 : 공중 유닛,수송기/공격x

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[player] 님이 게임에서 퇴장하셨습니다.")


game_start()
m1 = marine()
m2 = marine()
m3 = marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()
#유닛 일괄 관리(생성된 유닛 append) 
attackunit = []
attackunit.append(m1)
attackunit.append(m2)
attackunit.append(m3)
attackunit.append(t1)
attackunit.append(t2)
attackunit.append(w1)

#전군이동
for unit in attackunit:
    unit.move("1시")

#탱크 시즌모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

#공격모드 준비(마린 : 스팀팩, 탱크 : 시즈, 레이스 : 클로킹)
for unit in attackunit:
    if isinstance(unit, marine): #서로 다른 unit 개체를 각각 클래스 인스턴스인지 확인
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

#전군 공격
for unit in attackunit:
    unit.attack("1시")

#전군 피해
for unit in attackunit:
    unit.damaged(randint(5,21)) #공격을 랜덤으로 받음(5~20)

#게임종료
game_over()