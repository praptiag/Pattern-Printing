"""
    1 
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
"""
row=5
for i in range(1,row+1):
    for j in range(i,row):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print('\n')