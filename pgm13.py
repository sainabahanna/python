text=input("enter a line of text:")
word=text.split()
count={}
for words in word:
 if words in count:
     count[words]+=1
 else:
      count[words]=1
print(count)
