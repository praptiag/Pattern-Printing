"""
  G G G G G G G 
    E E E E E
      C C C
        A
"""
row=4
for i in range(row,0,-1):
    for space in range(i,row+1):
        print(" ",end=" ")
    for syb in range((2*i)-1,0,-1):
        print(chr(64+(2*i)-1),end=" ")
    print("\n")