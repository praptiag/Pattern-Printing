"""
*******
 *   *
  * *
   *
"""
row=4
for i in range(row,0,-1):
    for j in range(row,i,-1):
        print(" ",end="")
    for k in range(0,2*i-1):
        if i==row  or k==0 or k==2*i-2:
            print("*",end="")
        else:
            print(" ",end="")
    print()