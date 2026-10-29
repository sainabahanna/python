def compare(s1,s2,n):
    return s1[:n]==s2[:n]
s1=input("enter 1st string")
s2=input("enter 2nd string")
n=int(input("enter n:"))
print(compare(s1,s2,n))
