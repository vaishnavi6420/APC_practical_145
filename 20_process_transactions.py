fn=input("Transaction file: "); dep=wd=bal=largest=0
with open(fn) as f:
 for line in f:
  k,a=line.strip().split(","); a=float(a); largest=max(largest,a); bal += a if k=="D" else -a; dep += a if k=="D" else 0; wd += a if k=="W" else 0
print("Total deposits:",dep,"\nTotal withdrawals:",wd,"\nFinal balance:",bal,"\nLargest transaction:",largest)
