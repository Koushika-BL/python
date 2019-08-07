tup=(20,44,5,5,30,16,12,16)
list1=list(tup)
list1.sort()
tup=tuple(list1)
for i in range(len(tup)-1):
    if tup[i]==tup[i+1]:
        print(tup[i])
