fn=input("Employee file: ")
def read():
 with open(fn) as f: return [(a,n,d,float(s)) for a,n,d,s in (x.strip().split(",") for x in f)]
r=read(); [print(x) for x in r]; print("Highest paid:",max(r,key=lambda x:x[3])); print("Average salary:",sum(x[3] for x in r)/len(r)); lim=float(input("Salary limit: ")); [print(x) for x in r if x[3]>lim]
