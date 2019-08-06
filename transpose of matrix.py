x=[[3,2],
   [5,7],
   [3,7]]
res=[[0,0,0],
     [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        res[j][i]=x[i][j]
for r in res:
    print(r)
