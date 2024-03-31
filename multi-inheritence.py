class A:
    def display(self):
        print("In am in A")

class B:
    def display(self):
        print("In am in B")

class C(A,B):
    pass
    #def display3(self):
        #super().display1()
        #super().display2()
       #print("In am in C")

ob1=C()
ob1.display()