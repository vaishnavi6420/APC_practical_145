fn=input("Book file: ")
def read():
 with open(fn) as f:return [x.strip().split(",") for x in f]
def save(r):
 with open(fn,"w") as f:[f.write(",".join(x)+"\n") for x in r]
while True:
 c=input("1 Add 2 Search 3 Issue 4 Return 5 Available 6 Exit: ")
 r=read()
 if c=="1": r.append([input("ID: "),input("Title: "),input("Author: "),"Available"]);save(r)
 elif c=="2":
  q=input("ID/title: ").lower();print(*[x for x in r if x[0]==q or x[1].lower()==q],sep="\n")
 elif c in ("3","4"):
  q=input("Book ID: ");
  for x in r:
   if x[0]==q:x[3]="Issued" if c=="3" else "Available"
  save(r)
 elif c=="5": print(*[x for x in r if x[3]=="Available"],sep="\n")
 elif c=="6": break
