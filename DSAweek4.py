from collections import deque

#def demonstrateList(list): 
list=[]
list.append("Apples") 
list.append("Oranges") 
list.append("Bananas") 
print(list) 
     
list.insert(1, "Pineapples") 
print(list) 

list.pop(2); 

print(list) 
print(len(list))

print("Using a regular list") 
print(list)



print("Now using a deque") 
d = deque(["BMW","AUDi","Tesla"]) 
print(d)