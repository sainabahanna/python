names=input("enter first names separated by space:").split()
count=0
for name in names:
   count +=name.lower().count('a')
print("number=",count)

