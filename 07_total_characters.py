fn=input("Enter file name: ")
with open(fn) as f: print("Total characters including spaces:",len(f.read()))
