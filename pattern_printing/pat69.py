"""
* * * * * 
 * * * *
  * * *
   * *
    *
"""
row=5
for i in range(0,row):
    for j in range(0,i):
        print(" ",end="")
    for k in range(row,i,-1):
        print("* ",end="")
    print('\n')