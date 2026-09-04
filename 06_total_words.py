fn=input("Enter file name: ")
with open(fn) as f: print("Total words:",len(f.read().split()))
