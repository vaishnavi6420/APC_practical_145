a=input("First file: "); b=input("Second file: ")
with open(a) as x,open(b) as y:A=x.readlines();B=y.readlines()
if A==B: print("Files are identical")
else:
 for i in range(max(len(A),len(B))):
  u=A[i].rstrip() if i<len(A) else "<missing>";v=B[i].rstrip() if i<len(B) else "<missing>"
  if u!=v: print("First difference at line",i+1);print(u);print(v);break
