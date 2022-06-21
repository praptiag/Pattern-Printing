"""
    * 
   * *
  * * *
 * * * *
* * * * *
"""
row=5
for i in range(0,row):
    for j in range(row-1,i,-1):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    print("\n")
