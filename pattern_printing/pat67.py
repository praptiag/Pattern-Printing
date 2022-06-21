"""
    A 
   B B
  C C C
 D D D D
E E E E E
"""
row=5
for i in range(1,row+1):
    for j in range(i,row):
        print(" ",end="")
    for k in range(0,i):
        print(chr(64+i),end=" ")
    print('\n')