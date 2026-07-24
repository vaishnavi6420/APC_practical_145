n1=int(input("Enter Number :"))
n2=int(input("Enter Number :"))
n3=int(input("Enter Number :"))
if(n1<n2 and n1<n3):
    print(n1,"is smaller than",n2,"and",n3)
elif(n2<n1 and n2<n3):
    print(n2,"is smaller than",n1,"and",n3)    
else:
    print(n3,"is smaller than",n1,"and",n2)
    
