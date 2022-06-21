"""
      *       
    * * *     
  *   *   *
* * * * * * *
  *   *   *
    * * *
      *
"""
#input should be odd number

n=7
num=n//2*3
for i in range(n):
    for j in range(n):
        #center horizontal,center vertical, upper left diagonal, bottom left diagonal, upper right diagonal, bottom right diagonal
        if i==n//2 or j==n//2 or i+j==n//2 or i-j==n//2 or j-i==n//2 or i+j==num:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()