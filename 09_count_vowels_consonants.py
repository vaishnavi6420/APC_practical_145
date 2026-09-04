fn=input("Enter file name: ")
with open(fn) as f: t=f.read().lower()
print("Vowels:",sum(c in "aeiou" for c in t)); print("Consonants:",sum(c.isalpha() and c not in "aeiou" for c in t))
