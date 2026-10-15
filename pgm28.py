a=int(input("enter strating :"))
b=int(input("enter end"))
for i in range(a,b+1):
 if 1000<=i<=9999:
   if all(int(d)%2==0for d in str(i)):
     if int(i**0.5)**2==i:
       print(i)

