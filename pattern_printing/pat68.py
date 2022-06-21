"""
    A 
   A B
  A B C
 A B C D
A B C D E
"""
row=5
for i in range(1,row+1):
    for j in range(i,row):
        print(" ",end="")
    for k in range(0,i):
        print(chr(65+k),end=" ")
    print('\n')