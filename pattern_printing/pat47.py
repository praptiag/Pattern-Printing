"""
  * * * * * * * 
    * * * * *
      * * *
        *
"""
row=5
for i in range(row,0,-1):
    for space in range(i,row+1):
        print(" ",end=" ")
    for syb in range((2*i)-1,0,-1):
        print("*",end=" ")
    print("\n")