
def frequencyCount(s):
    d=dict()

    for c in s:
      if c in d:
        d[c]=d[c]+1
    else:
        d[c]=1
    return d


def makeTTString():
    table=2
    s=""
    while table<=12:
        mult=1
        while mult<=12:
            s=s+str(mult)+" times "+str(table)+" is "+str(mult*table)+("")
            mult=mult+1
        table=table+1
    return s

s=makeTTString()
print(s)

d=frequencyCount(s)
print()
print("Frequency map: ")
for k,v in d.items():
   print(k,v)

def sortedByValue(d):
   name=[]
   for k,v in d.items():
      name.append((v,k))
      return sorted(name,reverse=True)

print()
print("Sorted By frequency: ")
name=sortedByValue(d)

for item in name:
   print(item[1],item[0])


