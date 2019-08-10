from collections import Counter
dict1={'a':12,'b':4}
dict2={'h':7,'b':5}
dict3=Counter(dict1)+Counter(dict2)
print(dict3)
