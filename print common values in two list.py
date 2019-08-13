list1=[1,3,6,78,35,55,24,88]
list2=[12,24,35,24,88,120,155,1]
list3=(set(list1)&set(list2))
list3=list(list3)
list3.sort()
print(list3)
