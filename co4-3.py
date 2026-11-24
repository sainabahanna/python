class Rectangle:
  def __init__(self,length,width):
    self.length=length
    self.width=width

  def area(self):
    return self.length*self.width
  

  def __lt__(self,other):
   return self.area() < other.area()
   
   

l1 = int(input("Enter length of first rectangle: "))
w1 = int(input("Enter width of first rectangle: "))

l2 = int(input("Enter length of second rectangle: "))
w2 = int(input("Enter width of second rectangle: "))
r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)
print("Area of first rectangle:", r1.area())
print("Area of second rectangle:", r2.area())

if r1 < r2:
    print("First rectangle has smaller area")
else:
    print("First rectangle does not have smaller area")
