list1=[4,6,7,5,11,9,13,2]
position=3-1
idx=0
len_list=(len(list1))
while len_list>0:
    idx=(position+idx)%len_list
    print(list1.pop(idx))
    len_list-=1
    
