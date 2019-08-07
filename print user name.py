mail=input("enter  a email id")
for i in range(0,len(mail)):
    
    if mail[i]=="@":
        break
    print(mail[i])
    
