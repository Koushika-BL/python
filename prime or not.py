n=int(input("enter a number greater than 1"))
for i in range(2,n):
    if n%i==0:
        print("not a prime")
        break
else:
    print(" prime num")
