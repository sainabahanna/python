a=list(map(int,input("enter numbers:").split()))
print("+ve numbers:",[x for x in a if x>0])
n=int(input("enter N:"))
print("squers:",[x*x for x in range(1,n+1)])
word=input("enter a word")
print("vowels;",[x for x in word if x in"aeiou AEIOU"])
print("ordinal values:",[ord(x) for x in word])

