s={'cat','dog'}
print(s)

s.add('add')
s.add('mouse')
print(s)

'cat' in s
'dog' in s

s=set()
s.add(6)
s.add(7)
print(s)
s={1,2,3,3,2,1,5,5,6}
print(s)


list1 = "Python sets are based on hash tables which means they store their items in no particular order".split() 
list2= "Python does not have a sorted set implementation in the core language".split() 

set1=set();
for i in list1:
    set1.add(i)
print(set1)


set2 = set(); 
for i in list2: 
    set2.add(i) 
print(set2) 


set3 = set(); 
for i in set1: 
      if (i in set2): 
        set3.add(i) 

for i in set2: 
  if (i in set1): 
    set3.add(i) 
print(set3) 




