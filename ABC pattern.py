a=int(input("enter a number"))
n=65
for i in range(0,a):
    for j in range(0,i+1):
        ch=chr(n)
        print(ch,end=" ")
        n=n+1
    print("\r")
