def interest(p,t,senior):
 if senior=="yes":
  r=12
 else:
  r=10
 return(p*t*r)/100
p=float(input("enter principal"))
t=float(input("enter time"))
senior=input("senior citizen(yes/no):")
print("simple interst=",interest(p,t,senior))
