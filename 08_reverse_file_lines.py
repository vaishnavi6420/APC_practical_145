fn=input("Enter file name: ")
with open(fn) as f: lines=f.readlines()
for line in reversed(lines): print(line.rstrip())
