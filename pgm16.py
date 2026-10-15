list1=input("enter colors for list1:").split()
list2=input("enter colors for list2:").split()
for color in list1:
 if color not in list2:
   print(color)
