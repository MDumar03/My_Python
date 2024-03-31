class About:
    roll=""
    reg=""
    result=""

    def __init__(self,roll,reg,result):
        self.roll=roll
        self.reg=reg
        self.result=result

    def display(self):
        print(f"Roll:{self.roll},Reg:{self.reg},Result :{self.result}")

Rahim=About(102,3.65,"A*")      
Rahim.display()

              
