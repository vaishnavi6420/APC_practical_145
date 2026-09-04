fn=input("Enter file name: "); info=input("Enter additional information: ")
with open(fn,"a") as f: f.write(info+"\n")
