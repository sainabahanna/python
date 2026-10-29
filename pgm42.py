def fact(n):
 f=1
 for i in range(1,n+1):
   f=f*i
 return f
n=int(input("enter number of terms:"))
total=0
for i in range(1,n+1):
  total=total+(i**i)/fact(i)
print("sum of serires=",total)
