fn=input("Attendance file: ")
with open(fn) as f:
 for line in f:
  roll,name,p,t=line.strip().split(","); pct=int(p)/int(t)*100; print(name,pct,"%", "Below 75%" if pct<75 else "")
