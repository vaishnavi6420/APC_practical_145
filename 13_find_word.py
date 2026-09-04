fn=input("Enter file name: "); word=input("Enter word: ").lower(); total=0; nums=[]
with open(fn) as f:
 for i,line in enumerate(f,1):
  n=line.lower().split().count(word)
  if n: total+=n; nums.append(i)
print("Occurrences:",total); print("Line numbers:",nums)
