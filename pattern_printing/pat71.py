"""
5 4 3 2 1 
 4 3 2 1
  3 2 1 
   2 1 
    1 
"""
row=5
for i in range(row,0,-1):
    for j in range(row,i,-1):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end=" ")
    print('\n')