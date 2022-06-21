"""
        * * * * 
      * * * *
    * * * *
  * * * *
"""
row=4
for i in range(0,row):
    for j in range(row,i,-1):
        print(" ",end=" ")
    for k in range(0,row):
        print("*",end=" ")
    print('\n')