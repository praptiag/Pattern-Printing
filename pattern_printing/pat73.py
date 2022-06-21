"""
E D C B A 
 D C B A
  C B A
   B A
    A
"""
row=5
for i in range(row,0,-1):
    for j in range(row,i,-1):
        print(" ",end="")
    for k in range(i,0,-1):
        print(chr(64+k),end=" ")
    print('\n')