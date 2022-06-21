"""
  A B C D E F G 
    A B C D E 
      A B C
        A
"""
row=4
for i in range(row,0,-1):
    for space in range(i,row+1):
        print(" ",end=" ")
    for syb in range (1,((2*i)-1)+1):
        print(chr(64+syb),end=" ")
    print("\n")
