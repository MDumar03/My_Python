try:
    num1=int(input("Enter number 1 : "))
    num2=int(input("Enter number 2 : "))
    result=num1/num2
    print(result)

except(ValueError,ZeroDivisionError):
    print("Wrong input")

finally:
    ("Thanks !!!")