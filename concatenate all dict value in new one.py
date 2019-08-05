dict1={3:5,5:8,7:4}
dict2={2:3,4:5,9:6}
dict3={4:9,0:7,8:1}
dict4={}
for d in (dict1,dict2,dict3):
    dict4.update(d)
print(dict4)
