class cal:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        result = [num1*i for i in range(2,num2)]
        print(result, end = " ")

class cal2(cal):
    def __init__(self,num1, num2,num3):
        cal.__init__(self,num1, num2)  #상속받을 값
        self.num3 = num3 #상속값을 제외한 값
        result2 = [num1*(num2+num3) for num3 in range(2,num3)]
        print(result2)


calc = cal2(5,10,2)
        
# gugu2 = cal(3,8)