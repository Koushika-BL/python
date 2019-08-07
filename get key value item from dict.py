dict1={1:11,2:22,3:33,4:44,5:55,6:66}
print("key value count")
for count,(key,value)in enumerate(dict1.items(),1):
    print(key,' ',value,' ',count)
           
