file=open("myself.txt","a")
#print(file.writable())
#print(file.readable())
#file.write("\nWaka Waka")     //"r" "w"
text=file.read()

#size=len(text)
#print(size)
print(text)
file.close()