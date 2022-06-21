"""
E E E E E 
 D D D D
  C C C
   B B
    A
"""
row=5
for i in range(row,0,-1):
    for j in range(row,i,-1):
        print(" ",end="")
    for k in range(i,0,-1):
        print(chr(64+i),end=" ")
    print('\n')