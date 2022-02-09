class unit:
    def __init__(self):
        print("unit 생성자")
    
class flyable:
    def __init__(self):
        print("flying 생성자")

# class flyableunit(unit,flyable):
#     def __init__(self):
#         super().__init__()

class flyableunit(flyable,unit): #super를 사용한 경우 ()안의 순서에 따라 값이 달라진다
    def __init__(self):
        # super().__init__()
        unit.__init__(self)
        flyable.__init__(self)
#드랍쉽
dropship = flyableunit()