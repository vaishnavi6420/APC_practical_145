import re
fn=input("Enter file name: ")
with open(fn) as f: words=re.findall(r"\w+",f.read().lower())
d={}
for x in words: d[x]=d.get(x,0)+1
print(d)
