a=input("First file: "); b=input("Second file: "); out=input("Output file: ")
with open(a) as x,open(b) as y,open(out,"w") as z:z.write(x.read()+"\n"+y.read())
