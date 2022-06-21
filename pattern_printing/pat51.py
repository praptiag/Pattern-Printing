"""
  D D D D D D D 
    C C C C C
      B B B
        A
"""
row=4
for i in range(row,0,-1):
    for space in range(i,row+1):
        print(" ",end=" ")
    for k in range(0,(2*i)-1):
        print(chr(64+i),end=" ")
    print("\n")