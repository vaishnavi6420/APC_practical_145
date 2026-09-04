fn=input("Enter file name: ")
with open(fn) as f: print("Total lines:",sum(1 for _ in f))
