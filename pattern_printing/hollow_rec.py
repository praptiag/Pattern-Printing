#hollow rectangle

"""
* * * * * 
*       *
*       *
* * * * *
"""
row=4
col=5
for i in range(0,row):
    for j in range(0,col):
        if(i==0 or i==row-1 or j==0 or j==col-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print('\n')