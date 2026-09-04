src=input("Input file: "); out=input("Output file: ")
with open(src) as a,open(out,"w") as b: b.write(a.read().upper())
