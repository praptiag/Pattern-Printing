"""
5 5 5 5 5 
 4 4 4 4
  3 3 3
   2 2
    1
"""
row=5
for i in range(row,0,-1):
    for j in range(row,i,-1):
        print(" ",end="")
    for k in range(0,i):
        print(i,end=" ")
    print('\n')
