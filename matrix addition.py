x=[[3,2,8],
   [5,7,4],
   [3,7,5]]
y=[[6,8,7],
   [5,8,8],
   [4,8,2]]
res=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j]=x[i][j]+y[i][j]
for r in res:
    print(r)
