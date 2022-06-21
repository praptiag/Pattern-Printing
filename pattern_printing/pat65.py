"""
    1 
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
"""
row=5
for i in range(1,row+1):
    for j in range(i,row):
        print(" ",end="")
    for k in range(1,i+1):
        print(i,end=" ")
    print('\n')