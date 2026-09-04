import re
fn=input("Enter file name: ")
with open(fn) as f: words=re.findall(r"[A-Za-z0-9]+",f.read())
print("Longest word:",max(words,key=len) if words else "None")
