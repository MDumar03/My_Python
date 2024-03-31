menu=["1-New List","2-Add item","3-Remove item","Quit"]
print(menu)

newlist=[]
num=input("Enter Any Number (1-4) : ")
while(num!="4"):
    
    if(num=="1"):
        print(newlist)
        num=input("Enter Any Number (1-4) : ")
    elif(num=="2"):
        item=input("Enter Item to Add : ")
        newlist.append(item)
        print(newlist)
        num=input("Enter Any Number (1-4) : ")
    elif(num=="3"):
        index=int(input("Enter Index Number to Remove : ")) 
        newlist.pop(index)  
        print(newlist)
        num=input("Enter Any Number (1-4) : ")
print("Good Bye")        



