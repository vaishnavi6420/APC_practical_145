fn=input("Enter input file: "); old=input("Word to replace: "); new=input("New word: "); out=input("Output file: ")
with open(fn) as f: t=f.read()
with open(out,"w") as f: f.write(t.replace(old,new))
