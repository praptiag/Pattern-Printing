"""
A B C D E 
 A B C D
  A B C
   A B
    A
"""
row=5
for i in range(row,0,-1):
    for j in range(row,i,-1):
        print(" ",end="")
    for k in range(0,i):
        print(chr(65+k),end=" ")
    print('\n')