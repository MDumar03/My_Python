print("Stack\n")

Languages =[]
Languages.append("C++")
Languages.append("Python")
Languages.append("Java")
Languages.append("HTMl")
#print(Languages)

Languages.pop()
print(Languages)
print("Top Language is : ",Languages[-1])

Languages.pop()
print(Languages)
print("Top Language is : ",Languages[-1])

Languages.pop()
print(Languages)
print("Top Language is : ",Languages[-1])


Languages.pop()
if not Languages:
    print("Nothing Left")