squere=lambda s:s*s
rectangle=lambda l,b:l*b
triangle=lambda b,h:0.5*b*h
s=float(input("enter side 0f squere"))
l=float(input("enter length 0f rectangle"))
b=float(input("enter bredth 0f rectangle"))
base=float(input("enter  base of rectangle"))
h=float(input("enter h 0f rectangle"))



print("Area of squere=",squere(s))

print("Area of  rectangle=",rectangle(l,b))
print("area of triangle=",triangle(base,h))


