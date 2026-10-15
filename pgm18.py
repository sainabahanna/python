numbers=list(map(int,input("enter numbers").split()))
for n in numbers[:]:
 if n%2==0:
   numbers.remove(n)
print("list after removing even no",numbers)
