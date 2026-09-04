src=input("Python source file: "); out=input("Output file: ")
with open(src) as a,open(out,"w") as b:
 for line in a:
  if not line.lstrip().startswith("#"): b.write(line.split("#",1)[0].rstrip()+"\n")
