fn=input("Enter file name: ")
with open(fn) as f: t=f.read()
print("Alphabets:",sum(c.isalpha() for c in t)); print("Digits:",sum(c.isdigit() for c in t)); print("Spaces:",sum(c.isspace() for c in t)); print("Special characters:",sum(not c.isalnum() and not c.isspace() for c in t))
