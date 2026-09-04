fn=input("Student records file: "); r=[]
with open(fn) as f:
 next(f)
 for line in f:
  a,n,m=line.strip().split(","); r.append((a,n,float(m)))
print("All records:"); [print(x) for x in r]
h=max(r,key=lambda x:x[2]); print("Highest:",h); print("Average:",sum(x[2] for x in r)/len(r)); print("Above 80:"); [print(x) for x in r if x[2]>80]
