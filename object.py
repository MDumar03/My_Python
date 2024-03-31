
#object
print("By Using Object")
class Student:
    roll=""
    gpa=""
    section=""

Rahim=Student()
Rahim.roll=101
Rahim.gpa=4.70
Rahim.section="A"
print(f"Roll : {Rahim.roll},GPA : {Rahim.gpa},Section : {Rahim.section}")

Karim=Student()
Karim.roll=102
Karim.gpa=4.78
Karim.section="B"
print(f"Roll : {Karim.roll},GPA : {Karim.gpa},Section : {Karim.section}")

print("\n")


print("By Using Method")
class about:
    roll=""
    gpa=""
    section=""


    def set_value(self,roll,gpa,section):
        self.roll=roll
        self.gpa=gpa
        self.section=section

    def display(self):
        print(f"Roll : {self.roll},GPA : {self.gpa},Section : {self.section}")

Saiful=about()
Saiful.set_value(104,4.76,"D")
Saiful.display()

Umar=about()
Umar.set_value(103,5.00,"C")
Umar.display()




