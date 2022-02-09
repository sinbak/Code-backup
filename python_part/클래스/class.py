# #마린
# name = "마린"
# hp = 40
# damage = 5
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# #탱크 : 공격유닛,텡크,일반모드/시즈모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(name,location,damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 :{2}]".format(name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"2시",tank_damage)

class unit:
    def __init__ (self,name,hp,damage): #__init__ : 파이썬에서 쓰이는 생성자
        self.name = name #self.변수명 >> 멤버변수 : 클래스 내에서 정의된 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))

marine1 = unit("마린",40,5) #객체(클래스로부터 만들어지는 것)
marine2 = unit("마린",40,5)
tank = unit("탱크",150,35)

#레이스
wraith1 = unit("레이스",80,5)
print("유닛이름 : {0}, 공격력 {1}".format(wraith1.name,wraith1.damage))

#mindcontrol
wraith2 = unit("빼앗은 레이스",80,5)
wraith2.clocking = True #clocking이라는 변수를 추가적으로 할당

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
