class Iphone():
    def __init__(self):
        print("I am in I Phone CLASS")

class Nokia(Iphone):
    def __init__(self):
        super().__init__()
        print("I am in Nokia CLASS") 

n=Nokia()



class shape:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

class triangle(shape):
    def area(self):
        area=0.5*self.num1*self.num2
        print("Triangle : ",area)

class ractangle(shape):
    def area(self):
        area=self.num1*self.num2
        print("Ractangle : ",area)


t1=triangle(23,56)
t1.area()


r1=ractangle(23,56)
r1.area()



