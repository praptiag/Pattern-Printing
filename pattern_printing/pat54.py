"""
* 
* *
* * *
* * * *
* * *
* *
*
"""
col=4
for i in range(1,col+1):
    for j in range(0,i):
        print("*",end=" ")
    print('\n')
for i in range(col-1,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("\n")