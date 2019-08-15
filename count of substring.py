from re import findall
str1="abcdcdcdc"
print(len(findall('(?=cdc)',str1)))

