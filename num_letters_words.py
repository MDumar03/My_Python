letter=0
numbers=0
words=0

text=input("Enter text here : ")


for i in text:
    i=i.lower()

    if(i>='a' and i<='z'):
        letter=letter+1

    elif(i>='0' and i<='9'):
        numbers=numbers+1

    elif(i==" "):
        words=words+1


print("Number Of letter : ",letter)
print("Number Of Numbers :",numbers)
print("Number Of Words : ",words)
length=len(text)
print("The Size of text is : ",length)