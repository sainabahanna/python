list1=list(map(int,input("enter first list:").split()))
list2=list(map(int,input("enter list2:").split()))
if len(list1)==len(list2):
   print("(a)list are of same length")
else:
        print("(a)list are not same length") 


if sum(list1)==len(list2):
   print("(b) lists sum to the same value")
else:
         print("(b) lists not sum to the same value")


if set(list1).intersection(set(list2)):
   print("(c)both lists conatin same vlue")
else:
       print("(c)both lists not conatin same vlue")


