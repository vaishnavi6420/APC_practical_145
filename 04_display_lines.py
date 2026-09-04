fn=input("Enter file name: ")
with open(fn) as f:
 for line in f: print(line.rstrip())
