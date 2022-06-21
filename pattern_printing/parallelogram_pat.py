"""
* * * * * 
  * * * * *
    * * * * *
      * * * * *
"""
row=4
col=5
for i in range(0,row):
    for j in range(0,i):
        print(" ",end=" ")
    for k in range(0,col):
        print("*",end=" ")
    print('\n')