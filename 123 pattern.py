a=int(input("enter a number"))
n=1
for i in range(0,a):
    for j in range(0,i+1):
        print(n,end=" ")
        n=n+1
    print()
