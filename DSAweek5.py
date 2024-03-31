'''
print("Stack\n")

lists=["Messi","Ronaldo","Neymar","Inesta","Kross"]
print(lists)

lists.append("Rakitic")
print(lists)

lists.pop()
print(lists)
'''
from collections import deque

print("Lab week-5")
q=deque()
lists=["Tom","Jerry","Quaker","Spike","Quaker"]
l=len(lists)
print(lists)
for i in range(0,l):
    while(l>0):
        lists.pop()
        print(lists)